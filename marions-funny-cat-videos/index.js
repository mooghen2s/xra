const fs = require('fs');
const axios = require('axios');

function createMarion(apiKey) {
    const getFunnyCatVideos = async (count) => {
        try {
            const response = await axios.get('https://www.googleapis.com/youtube/v3/search', {
                params: {
                    part: 'snippet',
                    q: 'funny cat',
                    type: 'video',
                    maxResults: count,
                    key: apiKey,
                }
            });
            return response.data.items.map(item => ({
                title: item.snippet.title,
                url: `https://www.youtube.com/watch?v=${item.id.videoId}`
            }));
        } catch (error) {
            throw new Error(error.response ? error.response.data.error.message : error.message);
        }
    };

    const exportFunnyCatVideosCSV = async (filename, count) => {
        const videos = await getFunnyCatVideos(count);
        const csvContent = videos.map(video => `"${video.title}","${video.url}"`).join('\n');
        fs.writeFileSync(filename, csvContent, 'utf8');
    };

    return {
        getFunnyCatVideos,
        exportFunnyCatVideosCSV,
    };
}

module.exports = createMarion;
