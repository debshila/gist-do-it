# gist-do-it
## Web app for multi-level text summary generation

People rarely read privacy policy documents. However, with the recent privacy breaches and GDPR coming into effect, individuals
are recognizing the need to examine privacy policies that they previously blindly trusted. 
To facilitate examination of privacy policies, this web app basically generates summaries for 
privacy policy documents by selecting the most important sentences from these documents. The app leverages the 
textrank algorithm as implemented by the gensim package (https://radimrehurek.com/gensim/summarization/summariser.html).

In addition, the app displays the results of an Latent Dirichlet Allocation (LDA) based topic model 
(https://radimrehurek.com/gensim/models/ldamodel.html) trained on > 1000 privacy policy documents (https://usableprivacy.org/data),
visualized using the pyLDAvis LDA visualizer (https://pyldavis.readthedocs.io/en/latest/readme.html#usage). This interactive
illustration basically displays the underlying themes in privacy policy documents grouped into topics, the relationship amongst
these topics (spatial proximity of the topics), and the top keywords from the topics.
