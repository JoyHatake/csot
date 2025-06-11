Started off with finding sentiment values
Used a label encoder on inferred company, also converted the label (likes) to log1p
With these I was able to bring down the rmse to around 3k
I used label encoder for day of the week, but later on changed to one hot encoding the day of the week, since that seemed better.
Instead of using company_encoded, I used company-wide average likes, since that gave similar rmse and was faster and less feature columns.

I tried to use a sentence transformer from sentence_transformers library ("MiniLM-L6-v2" model), but that ended up increasing my rmse.
I then used a tf idf vectorizer instead and that decreased my rmse ever so slightly.
Currently my api is using the model without the tf_idf feature, I might change that later.


