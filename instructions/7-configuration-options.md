## 7. Configuration Options and Design Choices

### Lambda Function Configuration Options

You may have noticed that at the top of the [lambda_function.py](../lambda_function.py) we have a "User Settings" section with two boolean values set to True by default. You may then be wondering, what do each of these options do?

```
# User Settings
frugality = True
single_item_feed = True
```

#### **frugality**
When set to ```True```, the "frugality" variable will change the S3 storage class of your .mp3 to use "S3 Intelligent Tiering". When using this S3 storage class, S3 will automatically move objects to a lower cost storage class depending upon their usage.

When it comes to flash briefing .mp3s then, Alexa will never play content that's older than 7 days. It's therefore reasonable to expect that any files you've uploaded that are older than 7 days old will see a decline in access.

By using "S3 Intelligent Tiering" then, you're allowing S3 to automtically move your .mp3s to lower cost storage classes as needed, rather than keeping all of your .mp3s in the most expensive "S3 Standard" storage class.

I you want to keep all of your .mp3s in the "S3 Standard" tier, or simply don't want your Lambda function changing storage classes on your behalf, change this setting to ```False```.

More information on S3 storage classes can be found here:
https://aws.amazon.com/s3/storage-classes/

#### **single_item_feed**
When set to ```True```, the "single_item_feed" variable will cause your flash briefing feed to only ever retain the most recent audio file.

Retaining only the single most recent item in your flash briefing feed is a very common use case, especially in situations where the content of the feed may quickly become out of date. For example, if you had a "Breaking News" flash briefing skill, it wouldn't make much sense to retain the old news from yesteday.

If you instead want your flash briefing feed to retain all items, change this setting to ```False```.

### Lambda Function Design Choices

#### **The titleText Value Is Derived From MP3 File Name**
The [sample code](../lambda_function.py#L53) operates on the assumption that the name of the .mp3 file that you upload is the titleText value that you want to use within your flash breifing's .json feed.

For example then, if you want the "titleText" of your feed item to be "Test Audio File", then the name of your .mp3 must be "Test Audio File.mp3".

#### **The redirectionUrl Value Is Static**

The "redirectionUrl" value of your flash briefing .json feed is derived from the "redirection_url" environment variable that was configured in your Lambda function under "Configuration > Environment variables".

Given that fact, every item in your flash briefing feed will have the same "redirectionUrl" value. Per Amazon's [Flash Briefing Skill API Feed Reference](https://developer.amazon.com/en-US/docs/alexa/flashbriefing/flash-briefing-skill-api-feed-reference.html#details) documentation, the "redirectionUrl" value "Provides the URL target for the Read More link in the Alexa app." Because the "redirectionUrl" is static in our setup, the URL you use must therefore be relevant to all potential items in your feed.