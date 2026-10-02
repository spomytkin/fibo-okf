---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This module contains ontologies of Transaction concepts based on the Resource, Events Agents (REA) ontology for
      transactions.
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://purl.org/dc/terms/license
    value: https://opensource.org/licenses/MIT
  - predicate: http://purl.org/dc/terms/title
    value: FIBO FND Transactions Module
  - predicate: http://purl.org/dc/terms/title
    value: Financial Industry Business Ontology (FIBO) Foundations (FND) Transactions Module
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: transactions ext module
  - predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: The content in this module is original conceptual content and does not extend any other module. Some of the concepts
      represented conceptually in this module have been replaced by partial representations of some transaction concepts in
      the Products and Services module, sometimes using different labels for similar or equivalent concepts. Much of the content
      in this module will still be referred to in other FIBO domains, and care is needed in determining whether to replace
      these references to something in Products and Services versus when to bring forward more of the content in this module.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2017-2023 EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Module
  related_to:
  - concept: /concepts/fibo/FND/TransactionsExt/MarketTransactions.md
    predicate: http://purl.org/dc/terms/hasPart
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/MarketTransactions/
  - concept: /concepts/fibo/FND/TransactionsExt/REATransactions.md
    predicate: http://purl.org/dc/terms/hasPart
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/REATransactions/
  - concept: /concepts/fibo/FND/TransactionsExt/SecuritiesTransactions.md
    predicate: http://purl.org/dc/terms/hasPart
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/SecuritiesTransactions/
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://spec.edmcouncil.org/fibo/
resource: https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/MetadataFNDTransactionsExt/TransactionsExtModule
sources:
- id: fibo-source-d0ccb5540d
  resource: references/fibo/FND/TransactionsExt/MetadataFNDTransactionsExt.rdf
  sha256: d0ccb5540d6a97b80e2405daf83467dcda49dde9d6e83eccbb89ae5b6c9c922d
  title: FIBO source FND/TransactionsExt/MetadataFNDTransactionsExt.rdf
title: transactions ext module
type: Ontology Individual
---

# transactions ext module

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/TransactionsExt/MetadataFNDTransactionsExt/TransactionsExtModule>

## Relationships

- **Related to**: [MarketTransactions](/concepts/fibo/FND/TransactionsExt/MarketTransactions.md)
- **Related to**: [REATransactions](/concepts/fibo/FND/TransactionsExt/REATransactions.md)
- **Related to**: [SecuritiesTransactions](/concepts/fibo/FND/TransactionsExt/SecuritiesTransactions.md)
- **See also**: [fibo](<https://spec.edmcouncil.org/fibo/>)

## Annotations

- **abstract**: This module contains ontologies of Transaction concepts based on the Resource, Events Agents (REA) ontology for transactions.
- **license**: https://opensource.org/licenses/MIT
- **title**: FIBO FND Transactions Module
- **title**: Financial Industry Business Ontology (FIBO) Foundations (FND) Transactions Module
- **label**: transactions ext module
- **editorialNote**: The content in this module is original conceptual content and does not extend any other module. Some of the concepts represented conceptually in this module have been replaced by partial representations of some transaction concepts in the Products and Services module, sometimes using different labels for similar or equivalent concepts. Much of the content in this module will still be referred to in other FIBO domains, and care is needed in determining whether to replace these references to something in Products and Services versus when to bring forward more of the content in this module.
- **copyright**: Copyright (c) 2017-2023 EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
