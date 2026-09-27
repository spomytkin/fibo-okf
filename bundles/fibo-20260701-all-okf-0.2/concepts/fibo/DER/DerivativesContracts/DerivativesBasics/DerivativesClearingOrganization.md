---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: derivatives clearing organization
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: clearing house that enables parties to substitute the credit of the DCO for the credit of the parties
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: DCO
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.cftc.gov/IndustryOversight/ClearingOrganizations/index.htm
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Substitution may be done through contract novation, for example. A derivatives clearing organization (DCO) also
      arranges or provides, on a multilateral basis, for the settlement or netting of obligations, or otherwise provides clearing
      services or arrangements that mutualize or transfer credit risk among participants.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: For options, the derivatives clearing organization is responsible for clearing transactions for put and call options
      on common stocks and other equity issues, stock indexes, foreign currencies, interest rate composites and single-stock
      futures.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/ClearingHouse.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/ClearingHouse
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/DerivativesClearingOrganization
sources:
- id: fibo-source-1d46ff62ed
  resource: references/fibo/DER/DerivativesContracts/DerivativesBasics.rdf
  sha256: 1d46ff62ed97b1b5c5efb22344dc4a795f3a38a6a7c8d99e40c825cc75a891cb
  title: FIBO source DER/DerivativesContracts/DerivativesBasics.rdf
- id: fibo-source-3e67c374be
  resource: references/fibo/DER/DerivativesContracts/Options.rdf
  sha256: 3e67c374be7e2c644c596d83a2efadb08b8ed189c20644396891cf12b1f37d30
  title: FIBO source DER/DerivativesContracts/Options.rdf
title: derivatives clearing organization
type: Ontology Class
---

# derivatives clearing organization

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/DerivativesBasics/DerivativesClearingOrganization>

## Definition

clearing house that enables parties to substitute the credit of the DCO for the credit of the parties

## Relationships

- **Subclass of**: [ClearingHouse](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/ClearingHouse.md)

## Annotations

- **label**: derivatives clearing organization
- **definition**: clearing house that enables parties to substitute the credit of the DCO for the credit of the parties
- **abbreviation**: DCO
- **adaptedFrom**: http://www.cftc.gov/IndustryOversight/ClearingOrganizations/index.htm
- **explanatoryNote**: Substitution may be done through contract novation, for example. A derivatives clearing organization (DCO) also arranges or provides, on a multilateral basis, for the settlement or netting of obligations, or otherwise provides clearing services or arrangements that mutualize or transfer credit risk among participants.
- **explanatoryNote** (en): For options, the derivatives clearing organization is responsible for clearing transactions for put and call options on common stocks and other equity issues, stock indexes, foreign currencies, interest rate composites and single-stock futures.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
