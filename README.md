# Automatically Generate A Flash Briefing JSON Feed For Audio Content

## Summary

You may have thought to yourself that an Alexa flash briefing skill would be a great way to distribute your audio content, and you'd be right! You may have then looked into [how to build a flash briefing skill](https://developer.amazon.com/en-US/docs/alexa/flashbriefing/steps-to-create-a-flash-briefing-skill.html) and been confronted with questions like "where would I host my audio files and feeds?" or "how can I make sure that my feed endpoint stays up to date and meets the formatting requirements?" 

This guide seeks to answer those questions by teaching you how to use AWS resources to generate a well formatted audio flash briefing feed and host your audio files. By the end of this guide, you'll have an easy to use setup where simply uploading your .mp3 audio content will automatically create and update a .json flash briefing feed which can be used in your flash briefing skill.


## Getting Started

The steps for this guide have been broken up into seven sequential easy to digest modules. To begin the walkthrough, just click the first module below:

[1. Create A Lambda Execution Role With Appropriate Permissions](./instructions/1-create-iam-role.md)<br />
[2. Create Your Lambda Function](./instructions/2-create-lambda-function.md)<br />
[3. Create Your S3 Bucket](./instructions/3-create-s3-bucket.md)<br />
[4. Configure Your S3 Bucket With Events](./instructions/4-configure-s3-bucket.md)<br />
[5. Configure Your Lambda Function](./instructions/5-configure-lambda-function.md)<br />
[6. Test Your Setup](./instructions/6-test-setup.md)<br />
[7. Extra Credit: Configuration Options & Design Choices](./instructions/7-configuration-options.md)<br />

## Additional Resources

### Community
* [Alexa Flash Briefing Skill API Developer Forums](https://amazon.developer.forums.answerhub.com/spaces/181/index.html)

### Documentation
* [Steps To Create A Flash Briefing Skill](https://developer.amazon.com/en-US/docs/alexa/flashbriefing/steps-to-create-a-flash-briefing-skill.html)
* [Flash Briefing Skill API Feed Reference](https://developer.amazon.com/en-US/docs/alexa/flashbriefing/flash-briefing-skill-api-feed-reference.html)