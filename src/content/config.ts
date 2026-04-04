import { defineCollection, z } from 'astro:content';
import { glob, file } from 'astro/loaders';

const outilsCollection = defineCollection({
  loader: glob({ pattern: '**/*.md', base: 'src/content/outils' }),
  schema: z.object({
    title: z.string().optional().default('Titre manquant'),
    slug: z.string().optional(),
    excerpt: z.string().optional().default(''),
    date: z.string().optional().default(''),
    featuredImage: z.string().optional(),
    categories: z.array(z.string()).optional().default([]),
    casUsage: z.array(z.string()).optional().default([]),
    link: z.string().optional(),
  }),
});

const articlesCollection = defineCollection({
  loader: glob({ pattern: '**/*.md', base: 'src/content/articles' }),
  schema: z.object({
    title: z.string().optional().default('Titre manquant'),
    slug: z.string().optional(),
    excerpt: z.string().optional().default(''),
    date: z.string().optional().default(''),
    featuredImage: z.string().optional(),
    categories: z.array(z.string()).optional().default([]),
    lang: z.string().optional(),
  }),
});

const categoriesCollection = defineCollection({
  loader: glob({ pattern: '**/*.json', base: 'src/content/categories' }),
  schema: z.object({
    name: z.string(),
    slug: z.string(),
    description: z.string().default(''),
    count: z.number().default(0),
    icon: z.string().default('🔧'),
  }),
});

const casUsageCollection = defineCollection({
  loader: glob({ pattern: '**/*.json', base: 'src/content/cas-usage' }),
  schema: z.object({
    name: z.string(),
    slug: z.string(),
    description: z.string().default(''),
    count: z.number().default(0),
    icon: z.string().default('🎯'),
  }),
});

const alternativesCollection = defineCollection({
  loader: glob({ pattern: '**/*.json', base: 'src/content/alternatives' }),
  schema: z.object({
    mainTool: z.string(),
    mainToolSlug: z.string(),
    tools: z.array(z.object({
      name: z.string(),
      slug: z.string(),
      description: z.string(),
      short_description: z.string(),
      logo_url: z.string(),
      website_url: z.string(),
      affiliate_url: z.string(),
      pricing_type: z.enum(['free', 'freemium', 'paid']),
      price_starting: z.string().default(''),
      rating: z.number(),
      pros: z.array(z.string()).default([]),
      cons: z.array(z.string()).default([]),
      features: z.array(z.string()).default([]),
    })),
  }),
});

export const collections = {
  outils: outilsCollection,
  articles: articlesCollection,
  categories: categoriesCollection,
  'cas-usage': casUsageCollection,
  alternatives: alternativesCollection,
};
