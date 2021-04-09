const Downloader = require('puppeteer/utils/ChromiumDownloader');
const {chromium_revision} = require('puppeteer/package.json').puppeteer;
const info = Downloader.revisionInfo(Downloader.currentPlatform(), chromium_revision);
console.log(info);