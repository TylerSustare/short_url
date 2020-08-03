# This service is live in a 'dev' stage. 


## Run tests with `$ make test`


### Entry point for the app is `handler.py` for anyone new to serverless

## Feel Free to test with a curl request like this

``` shell
$ curl -d '{"url":"https://google.com"}' -H 'Content-Type: application/json' -X POST https://pnh85koiz6.execute-api.us-west-2.amazonaws.com/dev/
```
### Responds with (prettified)
``` JSON 
{
    "shortUrl": "https://pnh85koiz6.execute-api.us-west-2.amazonaws.com/dev/wmHQd"
}
```

## Then navigate to the "short" url and be amazed at the redirection!
