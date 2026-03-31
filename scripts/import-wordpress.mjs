#!/usr/bin/env node

/**
 * Script d'import WordPress → Astro Content Collections
 *
 * Ce script récupère TOUT le contenu de l'API WordPress headless
 * et le convertit en fichiers Markdown/JSON pour les Content Collections d'Astro.
 *
 * Usage:
 *   node scripts/import-wordpress.mjs
 *
 * Pré-requis:
 *   - API WordPress accessible à WP_BASE
 *   - Dossier iatechnologie-astro/ existant
 *
 * Ce qu'il fait:
 *   1. Récupère tous les outils (CPT "outils") avec pagination
 *   2. Récupère tous les articles (posts) avec pagination
 *   3. Récupère toutes les taxonomies (categorie-outil, cas-usage)
 *   4. Télécharge TOUTES les images (featured + embedded) dans public/images/
 *   5. Réécrit les URLs des images dans le HTML
 *   6. Réécrit les liens internes (iatechnologie.com/outil/... → /outil/...)
 *   7. Génère les fichiers .md et .json
 */

import fs from 'node:fs';
import path from 'node:path';
import https from 'node:https';
import http from 'node:http';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '..');

// ─── Configuration ───────────────────────────────────────────────
const WP_BASE = 'https://iatechnologie.com/wp-json';
const SITE_DOMAIN = 'iatechnologie.com';

const DIRS = {
  outils: path.join(ROOT, 'src/content/outils'),
  articles: path.join(ROOT, 'src/content/articles'),
  categories: path.join(ROOT, 'src/content/categories'),
  casUsage: path.join(ROOT, 'src/content/cas-usage'),
  alternatives: path.join(ROOT, 'src/content/alternatives'),
  imagesOutils: path.join(ROOT, 'public/images/outils'),
  imagesBlog: path.join(ROOT, 'public/images/blog'),
};

// ─── Helpers ─────────────────────────────────────────────────────

function ensureDirs() {
  Object.values(DIRS).forEach((dir) => {
    fs.mkdirSync(dir, { recursive: true });
  });
  console.log('✅ Directories created');
}

function fetchJson(url) {
  return new Promise((resolve, reject) => {
    const client = url.startsWith('https') ? https : http;
    client.get(url, { headers: { 'User-Agent': 'IA-Tech-Import/1.0' } }, (res) => {
      if (res.statusCode !== 200) {
        reject(new Error(`HTTP ${res.statusCode} for ${url}`));
        res.resume();
        return;
      }
      let data = '';
      res.on('data', (chunk) => (data += chunk));
      res.on('end', () => {
        try {
          resolve({ json: JSON.parse(data), headers: res.headers });
        } catch (e) {
          reject(new Error(`JSON parse error for ${url}: ${e.message}`));
        }
      });
    }).on('error', reject);
  });
}

async function fetchAllPages(endpoint) {
  const results = [];
  let page = 1;
  let totalPages = 1;

  while (page <= totalPages) {
    const url = `${WP_BASE}${endpoint}${endpoint.includes('?') ? '&' : '?'}per_page=100&page=${page}&_embed=true`;
    console.log(`  📄 Fetching page ${page}/${totalPages}: ${url}`);
    try {
      const { json, headers } = await fetchJson(url);
      results.push(...json);
      totalPages = parseInt(headers['x-wp-totalpages'] || '1', 10);
      page++;
    } catch (e) {
      console.error(`  ❌ Error fetching page ${page}: ${e.message}`);
      break;
    }
  }

  console.log(`  ✅ Total items fetched: ${results.length}`);
  return results;
}

function downloadFile(url, destPath) {
  return new Promise((resolve, reject) => {
    if (fs.existsSync(destPath)) {
      resolve(destPath);
      return;
    }
    const dir = path.dirname(destPath);
    fs.mkdirSync(dir, { recursive: true });

    const client = url.startsWith('https') ? https : http;
    client.get(url, { headers: { 'User-Agent': 'IA-Tech-Import/1.0' } }, (res) => {
      if (res.statusCode === 301 || res.statusCode === 302) {
        downloadFile(res.headers.location, destPath).then(resolve).catch(reject);
        return;
      }
      if (res.statusCode !== 200) {
        reject(new Error(`HTTP ${res.statusCode} downloading ${url}`));
        res.resume();
        return;
      }
      const ws = fs.createWriteStream(destPath);
      res.pipe(ws);
      ws.on('finish', () => { ws.close(); resolve(destPath); });
      ws.on('error', reject);
    }).on('error', reject);
  });
}

function slugify(text) {
  return text
    .toString()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/(^-|-$)/g, '');
}

function sanitizeFilename(url) {
  const parsed = new URL(url);
  const filename = path.basename(parsed.pathname);
  return filename.replace(/[^a-zA-Z0-9._-]/g, '_');
}

// ─── Image Processing ────────────────────────────────────────────

async function downloadAndRewriteImages(htmlContent, imageDir, imageUrlPrefix) {
  // Find all image URLs in the HTML
  const imgRegex = /(?:src|srcset)=["']([^"']+?(?:\.png|\.jpg|\.jpeg|\.gif|\.webp|\.svg|\.avif)[^"']*?)["']/gi;
  const wpContentRegex = /https?:\/\/[^"'\s]+?\/wp-content\/uploads\/[^"'\s]+?(?:\.png|\.jpg|\.jpeg|\.gif|\.webp|\.svg|\.avif)/gi;

  const allUrls = new Set();

  // Extract from src/srcset
  let match;
  while ((match = imgRegex.exec(htmlContent)) !== null) {
    // Handle srcset (multiple URLs separated by commas)
    const urls = match[1].split(',').map((u) => u.trim().split(/\s+/)[0]);
    urls.forEach((u) => allUrls.add(u));
  }

  // Extract wp-content URLs
  while ((match = wpContentRegex.exec(htmlContent)) !== null) {
    allUrls.add(match[0]);
  }

  let result = htmlContent;
  const downloadPromises = [];

  for (const imageUrl of allUrls) {
    if (!imageUrl.startsWith('http')) continue;

    const filename = sanitizeFilename(imageUrl);
    const destPath = path.join(imageDir, filename);
    const newUrl = `${imageUrlPrefix}/${filename}`;

    downloadPromises.push(
      downloadFile(imageUrl, destPath)
        .then(() => {
          console.log(`    🖼️  Downloaded: ${filename}`);
        })
        .catch((e) => {
          console.error(`    ⚠️  Failed to download ${imageUrl}: ${e.message}`);
        })
    );

    // Rewrite URL in content
    result = result.replaceAll(imageUrl, newUrl);
  }

  await Promise.allSettled(downloadPromises);
  return result;
}

// ─── Internal Link Rewriting ─────────────────────────────────────

function rewriteInternalLinks(htmlContent) {
  // Rewrite links like https://iatechnologie.com/outil/... → /outil/...
  // And https://cms.iatechnologie.com/... → local equivalents
  let result = htmlContent;

  // Domain patterns to rewrite
  const domains = [
    `https://${SITE_DOMAIN}`,
    `http://${SITE_DOMAIN}`,
    `https://cms.${SITE_DOMAIN}`,
    `http://cms.${SITE_DOMAIN}`,
    `https://www.${SITE_DOMAIN}`,
    `http://www.${SITE_DOMAIN}`,
  ];

  for (const domain of domains) {
    // Replace href="https://iatechnologie.com/outil/chatgpt" → href="/outil/chatgpt"
    const hrefRegex = new RegExp(`href=["']${domain.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}(/[^"']*?)["']`, 'gi');
    result = result.replace(hrefRegex, (match, path) => {
      return `href="${path}"`;
    });
  }

  return result;
}

// ─── Extract Featured Image ─────────────────────────────────────

function getFeaturedImageUrl(item) {
  try {
    if (item._embedded?.['wp:featuredmedia']?.[0]?.source_url) {
      return item._embedded['wp:featuredmedia'][0].source_url;
    }
    if (item._embedded?.['wp:featuredmedia']?.[0]?.media_details?.sizes?.full?.source_url) {
      return item._embedded['wp:featuredmedia'][0].media_details.sizes.full.source_url;
    }
  } catch { }
  return null;
}

// ─── Taxonomy Extraction ─────────────────────────────────────────

function getTermSlugs(item, taxonomyIndex) {
  try {
    const terms = item._embedded?.['wp:term']?.[taxonomyIndex] || [];
    return terms.map((t) => t.slug);
  } catch {
    return [];
  }
}

// ─── WordPress Import ────────────────────────────────────────────

async function importOutils() {
  console.log('\n🔧 Importing Outils...');
  const outils = await fetchAllPages('/wp/v2/outils');

  for (const outil of outils) {
    const slug = outil.slug;
    const title = outil.title?.rendered || outil.title || '';
    const excerpt = (outil.excerpt?.rendered || '').replace(/<[^>]*>/g, '').trim();
    const date = outil.date || '';
    const content = outil.content?.rendered || '';
    const categories = getTermSlugs(outil, 0); // categorie-outil
    const casUsage = getTermSlugs(outil, 1); // cas-usage
    const featuredImageUrl = getFeaturedImageUrl(outil);
    const link = outil.acf?.lien_outil || outil.acf?.link || '';

    // Download & rewrite images
    let processedContent = await downloadAndRewriteImages(content, DIRS.imagesOutils, '/images/outils');
    processedContent = rewriteInternalLinks(processedContent);

    // Download featured image
    let featuredImageLocal = '';
    if (featuredImageUrl) {
      const filename = sanitizeFilename(featuredImageUrl);
      const destPath = path.join(DIRS.imagesOutils, filename);
      try {
        await downloadFile(featuredImageUrl, destPath);
        featuredImageLocal = `/images/outils/${filename}`;
        console.log(`    🖼️  Featured: ${filename}`);
      } catch (e) {
        console.error(`    ⚠️  Failed featured image: ${e.message}`);
      }
    }

    // Generate Markdown
    const frontmatter = [
      '---',
      `title: "${title.replace(/"/g, '\\"')}"`,
      `slug: "${slug}"`,
      `excerpt: "${excerpt.replace(/"/g, '\\"')}"`,
      `date: "${date}"`,
      featuredImageLocal ? `featuredImage: "${featuredImageLocal}"` : null,
      `categories: [${categories.map((c) => `"${c}"`).join(', ')}]`,
      `casUsage: [${casUsage.map((c) => `"${c}"`).join(', ')}]`,
      link ? `link: "${link}"` : null,
      '---',
    ].filter(Boolean).join('\n');

    const mdContent = `${frontmatter}\n\n${processedContent}\n`;
    const filePath = path.join(DIRS.outils, `${slug}.md`);
    fs.writeFileSync(filePath, mdContent, 'utf-8');
    console.log(`  ✅ ${slug}.md`);
  }

  return outils.length;
}

async function importArticles() {
  console.log('\n📝 Importing Articles...');
  const posts = await fetchAllPages('/wp/v2/posts');

  for (const post of posts) {
    const slug = post.slug;
    const title = post.title?.rendered || post.title || '';
    const excerpt = (post.excerpt?.rendered || '').replace(/<[^>]*>/g, '').trim();
    const date = post.date || '';
    const content = post.content?.rendered || '';
    const categories = getTermSlugs(post, 0);
    const featuredImageUrl = getFeaturedImageUrl(post);

    // Download & rewrite images
    let processedContent = await downloadAndRewriteImages(content, DIRS.imagesBlog, '/images/blog');
    processedContent = rewriteInternalLinks(processedContent);

    // Download featured image
    let featuredImageLocal = '';
    if (featuredImageUrl) {
      const filename = sanitizeFilename(featuredImageUrl);
      const destPath = path.join(DIRS.imagesBlog, filename);
      try {
        await downloadFile(featuredImageUrl, destPath);
        featuredImageLocal = `/images/blog/${filename}`;
        console.log(`    🖼️  Featured: ${filename}`);
      } catch (e) {
        console.error(`    ⚠️  Failed featured image: ${e.message}`);
      }
    }

    // Generate Markdown
    const frontmatter = [
      '---',
      `title: "${title.replace(/"/g, '\\"')}"`,
      `slug: "${slug}"`,
      `excerpt: "${excerpt.replace(/"/g, '\\"')}"`,
      `date: "${date}"`,
      featuredImageLocal ? `featuredImage: "${featuredImageLocal}"` : null,
      `categories: [${categories.map((c) => `"${c}"`).join(', ')}]`,
      '---',
    ].filter(Boolean).join('\n');

    const mdContent = `${frontmatter}\n\n${processedContent}\n`;
    const filePath = path.join(DIRS.articles, `${slug}.md`);
    fs.writeFileSync(filePath, mdContent, 'utf-8');
    console.log(`  ✅ ${slug}.md`);
  }

  return posts.length;
}

async function importTaxonomies() {
  console.log('\n🏷️  Importing Taxonomies...');

  // Category icons mapping (best-effort, customize as needed)
  const defaultIcons = {
    video: '🎬', image: '🖼️', audio: '🎵', texte: '✍️', code: '💻',
    marketing: '📈', productivite: '⚡', education: '🎓', design: '🎨',
    finance: '💰', sante: '🏥', musique: '🎶', photo: '📷', seo: '🔍',
    chatbot: '💬', email: '📧', presentation: '📊', traduction: '🌍',
    recherche: '🔬', resume: '📋', ecriture: '✏️', rh: '👥',
  };

  // Categories
  try {
    const categories = await fetchAllPages('/wp/v2/categorie-outil');
    for (const cat of categories) {
      const iconKey = Object.keys(defaultIcons).find((k) => cat.slug.includes(k));
      const data = {
        name: cat.name,
        slug: cat.slug,
        description: (cat.description || '').replace(/<[^>]*>/g, '').trim(),
        count: cat.count || 0,
        icon: defaultIcons[iconKey] || '🔧',
      };
      const filePath = path.join(DIRS.categories, `${cat.slug}.json`);
      fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf-8');
      console.log(`  ✅ Category: ${cat.slug}`);
    }
  } catch (e) {
    console.error(`  ❌ Error importing categories: ${e.message}`);
  }

  // Cas d'usage
  try {
    const casUsages = await fetchAllPages('/wp/v2/cas-usage');
    for (const cu of casUsages) {
      const data = {
        name: cu.name,
        slug: cu.slug,
        description: (cu.description || '').replace(/<[^>]*>/g, '').trim(),
        count: cu.count || 0,
        icon: '🎯',
      };
      const filePath = path.join(DIRS.casUsage, `${cu.slug}.json`);
      fs.writeFileSync(filePath, JSON.stringify(data, null, 2), 'utf-8');
      console.log(`  ✅ Cas d'usage: ${cu.slug}`);
    }
  } catch (e) {
    console.error(`  ❌ Error importing cas d'usage: ${e.message}`);
  }
}

// ─── Main ────────────────────────────────────────────────────────

async function main() {
  console.log('╔══════════════════════════════════════════════╗');
  console.log('║  IA Technologie — WordPress → Astro Import  ║');
  console.log('╚══════════════════════════════════════════════╝');

  ensureDirs();

  try {
    const outilCount = await importOutils();
    const articleCount = await importArticles();
    await importTaxonomies();

    console.log('\n╔══════════════════════════════════════════════╗');
    console.log('║  ✅ Import terminé !                         ║');
    console.log(`║  📦 Outils: ${String(outilCount).padEnd(34)}║`);
    console.log(`║  📝 Articles: ${String(articleCount).padEnd(32)}║`);
    console.log('║                                              ║');
    console.log('║  Prochaine étape:                            ║');
    console.log('║  npm run dev                                 ║');
    console.log('╚══════════════════════════════════════════════╝');
  } catch (e) {
    console.error('\n❌ Import failed:', e.message);
    console.error('\nSi l\'API WordPress est inaccessible (erreur 525),');
    console.error('vous pouvez exporter les données via:');
    console.error('  1. WP-CLI: wp export --dir=./export');
    console.error('  2. phpMyAdmin: export JSON');
    console.error('  3. Plugin WP All Export');
    process.exit(1);
  }
}

main();
