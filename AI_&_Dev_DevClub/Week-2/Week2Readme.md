Started off with finding sentiment values
Then used a label encoder on inferred company, also converted the label (likes) to log
With these I was able to bring down the rmse to around 3k
I then one hot encoded the day of the week and also instead of using company_encoded, I used company-wide average likes

I tried to use a sentence transformer from sentence_transformers library ("MiniLM-L6-v2" model), but that ended up increasing my rmse.


