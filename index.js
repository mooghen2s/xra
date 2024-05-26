const createMarion = require("./marions-funny-cat-videos");

const YOUTUBE_API_KEY = process.env.YOUTUBE_API_KEY;

if (!YOUTUBE_API_KEY) {
    console.error("YOUTUBE_API_KEY is not set.");
    process.exit(1);
}

// Create the instance of Marion
const marion = createMarion(YOUTUBE_API_KEY);

// Get some funny cat videos
marion.getFunnyCatVideos(3)
    .then(videoList => {
        console.log("videoList", videoList);
    })
    .catch(err => {
        console.error(err);
    });

// Export CSV
marion.exportFunnyCatVideosCSV("funny_cat_videos.csv", 3);
