#!/usr/bin/env node

/**
 * Script pour récupérer les données en direct de la chaîne YouTube
 * et mettre à jour src/data/youtube-videos.json
 * 
 * Usage:
 *   YOUTUBE_API_KEY="ta_cle_api" node scripts/fetch-youtube.mjs
 */

import fs from 'node:fs';
import path from 'node:path';
import https from 'node:https';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const DATA_FILE = path.resolve(__dirname, '../src/data/youtube-videos.json');

// Remplace par ton ID de chaîne si tu le connais (celui qui commence par UC...)
// Pour iatechnologie-com, il faudra l'ID de la chaîne
const CHANNEL_ID = 'UC_XXXXXXXXXXXXXX'; // À CHANGER
const API_KEY = process.env.YOUTUBE_API_KEY;

if (!API_KEY) {
  console.error('❌ Erreur: La variable d\'environnement YOUTUBE_API_KEY est requise.');
  console.log('Obtenez une clé ici : https://console.cloud.google.com/apis/library/youtube.googleapis.com');
  process.exit(1);
}

function fetchJson(url) {
  return new Promise((resolve, reject) => {
    https.get(url, (res) => {
      let data = '';
      res.on('data', (chunk) => data += chunk);
      res.on('end', () => {
        try { resolve(JSON.parse(data)); }
        catch (e) { reject(e); }
      });
    }).on('error', reject);
  });
}

async function main() {
  console.log('Récupération des données YouTube en cours...');

  try {
    // 1. Fetch channel stats (subscribers)
    const channelUrl = `https://www.googleapis.com/youtube/v3/channels?part=statistics,snippet&id=${CHANNEL_ID}&key=${API_KEY}`;
    const channelData = await fetchJson(channelUrl);
    
    if (!channelData.items || channelData.items.length === 0) {
      throw new Error("Chaîne introuvable. Vérifiez le CHANNEL_ID.");
    }

    const subCount = parseInt(channelData.items[0].statistics.subscriberCount, 10);
    const channelName = channelData.items[0].snippet.title;

    // 2. Fetch latest videos
    const searchUrl = `https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=${CHANNEL_ID}&maxResults=6&order=date&type=video&key=${API_KEY}`;
    const searchData = await fetchJson(searchUrl);

    const videos = searchData.items.map(item => ({
      id: item.id.videoId,
      title: item.snippet.title,
      thumbnail: item.snippet.thumbnails.medium.url,
      publishedAt: item.snippet.publishedAt,
      description: item.snippet.description
    }));

    // 3. Save to file
    const output = {
      subscriberCount: subCount,
      channelName: channelName,
      videos: videos
    };

    fs.writeFileSync(DATA_FILE, JSON.stringify(output, null, 2), 'utf-8');
    console.log(`✅ Succès ! ${subCount} abonnés et ${videos.length} vidéos enregistrés.`);
    
  } catch (error) {
    console.error('❌ Erreur lors de la récupération YouTube :', error.message);
  }
}

main();
