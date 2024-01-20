<h2 style="text-align:center;">NLP Zero-shot Classification:</h2>
<p style="text-align:center;"><strong>M.Sc Marcello Barretto</strong></p>
<p style="text-align:center; font-size: 0.9em; margin-top: -10px;">Collège O'Sullivan de Québec</p>
<p style="text-align:center;font-size: 0.8em; margin-top: -10px;font-style:italic;">{mabarretto}@osullivan-quebec.qc.ca</p>
<h4 style="text-align:center; font-weight:bold;font-style:italic;">Abstract</h4>
<p style="text-align:justify; font-size:0.8em; font-style:italic;">This paper delves into the innovative realm of zero-shot classification (ZSC) in NLP, focusing on its application via transformer models like BERT and XLM-R. ZSC represents a paradigm shift in machine learning, enabling models to classify content beyond their explicit training, thus breaking the conventional reliance on large labelled datasets. The paper explores diverse use cases, including social media data using knowledge graph embedding, automated abstract screening in healthcare, and requirements classification in software engineering. As ZSC continues to evolve, it promises even broader applications and more profound impacts on data processing and analysis.</p>

#### 1. Introduction

<p style="text-align:justify;font-size;">Over the past few years NLP has been revolutionized by a new paradigm - zero-shot classification (ZSC). ZSC as its name suggests, is a method where models can classify content they have not been explicitly trained for. Traditionally, machine learning models require large amounts of labelled data to learn from and perform well. However, ZSC breaks this barrier by leveraging transformers, such as BERT and XLM-R, to understand and classify data in ways it has not been directly trained to handle. This offers great potential for numerous applications across different industries.</p>


#### 2. The Concept of Zero-shot Classification

<p style="text-align:justify; font-size;">Zero-shot classification refers to the ability of a model to infer classes that it has not seen during training. In NLP, this translates to assigning a label to a text based on its semantic content without prior exposure to examples of that class during training. Essentially, the model learns how to codify a question and find its answer within the text [^5^].</p>

#### 3. Use Cases

<p style="text-align:justify; font-size;">One application of zero-shot classification is in the analysis of social media data. Traditional methods often struggle with the volume and variety of user-generated content on these platforms. However, by using knowledge graph embedding, zero-shot text classification can categorize posts without needing explicit training on each possible category [^1^].

In the healthcare sector, systematic reviews demand the collection, evaluation, and synthesis of vast volumes of literature - a process that's both time-consuming and subjective. Zero-shot classification offers an automated solution for abstract screening. By learning to identify relevant criteria within abstracts without prior training, it can streamline the review process significantly [^5^].

Within software engineering, requirement gathering can be enhanced using zero-shot classification technology as well. When classifying functional requirements vs non-functional requirements or identifying specific classes of non-functional requirements (NFR), zero-shot learning algorithms can outperform traditional methods without any task-specific labelled training data [^4^].</p>


#### 4.Transformers in Zero-shot Classification

<p style="text-align:justify; font-size;">Transformers such as BERT (Bidirectional Encoder Representations from Transformers) and XLM-R (Cross-lingual Language Model) form the foundation of zero-shot classification in NLP. Pre-trained on large corpora, these models capture contextual relationships between words within sentences across multiple languages2.

BERT, for instance, is pre-trained in over 100 languages and can be fine-tuned by adding an output layer for tasks like question answering or abstract summarization. Similarly, XLM-R is trained across around 100 languages and doesn't require a language tensor to determine which language is being used [^2^].</p>


#### 5. Conclusion

The advent of zero-shot classification presents new opportunities for many industries grappling with unlabelled data or rapidly evolving datasets that are challenging to keep up with via traditional learning methods. By leveraging pre-trained transformer models like BERT and XLM-R, zero-shot classification paves the way for novel applications in NLP, including social media text classification, abstract screening in systematic reviews, and requirements classification in software engineering. As research progresses, we can expect to see more innovative uses for this promising technology. [^1^] [^2^] [^3^] [^4^] [^5^].

#### 6. BibTeX

<p style="font-size: 0.7em; margin-top: -10px;">
- - - </p>

<p style="font-size: 0.7em; margin-top: -10px;">
@misc{Collège O'Sullivan de Québec,</p>
<p style="font-size: 0.7em; margin-top: -10px;">
  author = {Marcello Barretto},</p>
<p style="font-size: 0.7em; margin-top: -10px;">
  title = {NLP, 2024},</p>
<p style="font-size: 0.7em; margin-top: -10px;">
  howpublished = "Collège O'Sullivan - e.Campus",</p>
<p style="font-size: 0.7em; margin-top: -10px;">
  year = {2024},</p>
<p style="font-size: 0.7em; margin-top: -10px;">
  note = "[GitHub Online; 420-T85-OQ]"}</p>

<p style="font-size: 0.7em; margin-top: -10px;">
- - - </p>

#### 7. References

[^1^]: [Zero-shot text classification via knowledge graph embedding for social media data](https://ieeexplore.ieee.org/abstract/document/9466939/)
[^2^]: [ZeroBERTo: Leveraging zero-shot text classification by topic modeling](https://link.springer.com/chapter/10.1007/978-3-030-98305-5_12)
[^3^]: [Zero-shot emotion detection for semi-supervised sentiment analysis using sentence transformers and ensemble learning](https://www.mdpi.com/2076-3417/12/17/8662)
[^4^]: [Zero-shot learning for requirements classification: An exploratory study](https://www.sciencedirect.com/science/article/pii/S0950584923000563)
[^5^]: [A novel application of machine learning and zero-shot classification methods for automated abstract screening in systematic reviews](https://www.sciencedirect.com/science/article/pii/S2772662223000024)






