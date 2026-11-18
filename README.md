# DROP IN — Advanced Snowboard + Skateboard Feed

Public static website powered by YouTube Data API v3 and GitHub Actions.

## Activate
1. Create a Google Cloud project at https://console.cloud.google.com/ and enable YouTube Data API v3.
2. Create an API key and restrict it to YouTube Data API v3. Do not restrict to a static IP or HTTP referrer, because the collector runs on GitHub-hosted runners.
3. In this repository go to Settings → Secrets and variables → Actions → New repository secret. Name it YOUTUBE_API_KEY.
4. Open Actions → Refresh DROP IN feed → Run workflow. Verify feed.json now has videos.
5. Go to Settings → Pages → Build and deployment → Deploy from a branch → main → /(root) → Save.
6. Visit https://dropinboards.github.io/dropin-video-hub/

The scheduled workflow refreshes every 6 hours, subject to GitHub scheduling delays. 12 YouTube search requests × 100 units × 4 runs = about 4,800 quota units/day. Results are filtered by topic and basic beginner-related phrases; they are not guaranteed to be exhaustive or exclusively professional.
