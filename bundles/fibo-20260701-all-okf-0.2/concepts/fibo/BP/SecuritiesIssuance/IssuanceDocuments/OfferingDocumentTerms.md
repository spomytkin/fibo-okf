---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: offering document terms
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: terms included in an offering document that become legally binding at issue
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: They include, for example, call terms, interest payment terms, and so forth with respect to certain securities.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractualElement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractualElement
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceDocuments/OfferingDocumentTerms
sources:
- id: fibo-source-4c4b98a252
  resource: references/fibo/BP/SecuritiesIssuance/IssuanceDocuments.rdf
  sha256: 4c4b98a25292417c0cfa751a871d67e42ea9e85f29ea26acb47bf9860bbda08e
  title: FIBO source BP/SecuritiesIssuance/IssuanceDocuments.rdf
title: offering document terms
type: Ontology Class
---

# offering document terms

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceDocuments/OfferingDocumentTerms>

## Definition

terms included in an offering document that become legally binding at issue

## Relationships

- **Subclass of**: [ContractualElement](/concepts/fibo/FND/Agreements/Contracts/ContractualElement.md)

## Annotations

- **label** (en): offering document terms
- **definition** (en): terms included in an offering document that become legally binding at issue
- **explanatoryNote** (en): They include, for example, call terms, interest payment terms, and so forth with respect to certain securities.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
