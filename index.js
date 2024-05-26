// index.js
const createMarion = require("./marions-funny-cat-videos");

const YOUTUBE_API_KEY = process.env.YOUTUBE_API_KEY;
const SEARCH_QUERY = process.env.SEARCH_QUERY || 'funny cat'; // Default to 'funny cat' if not set
const COUNT = parseInt(process.env.COUNT, 10) || 5; // Default to 5 if not set or not a valid number

if (!YOUTUBE_API_KEY) {
    console.error("YOUTUBE_API_KEY is not set.");
    process.exit(1);
}

// Create the instance of Marion
const marion = createMarion(YOUTUBE_API_KEY);

// Get some funny cat videos
marion.getFunnyCatVideos(SEARCH_QUERY, COUNT)
    .then(videoList => {
        console.log("videoList", videoList);
    })
    .catch(err => {
        console.error(err);
    });

// Export CSV
marion.exportFunnyCatVideosCSV("funny_cat_videos.csv", SEARCH_QUERY, COUNT);
