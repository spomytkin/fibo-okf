---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: custodian
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial institution that holds customers' securities for safekeeping
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.investopedia.com/terms/c/custodian.asp
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The custodian may hold stocks or other assets in electronic or physical form for mutual funds, individuals, and
      organizational clients.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Share
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/holds
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ThirdPartyAgent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ThirdPartyAgent
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Custodian
sources:
- id: fibo-source-1c0f41de59
  resource: references/fibo/SEC/Equities/EquityInstruments.rdf
  sha256: 1c0f41de59ed514a1c80cfea5fbe96be6493eea8266f851de2d3bbd414fdcd32
  title: FIBO source SEC/Equities/EquityInstruments.rdf
title: custodian
type: Ontology Class
---

# custodian

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/EquityInstruments/Custodian>

## Definition

financial institution that holds customers' securities for safekeeping

## Relationships

- **Subclass of**: [FinancialInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/FinancialInstitution.md)
- **Subclass of**: [ThirdPartyAgent](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/ThirdPartyAgent.md)

## Constraints

- **[holds](/concepts/fibo/FND/Relations/Relations/holds.md)**: some values from of type [Share](/concepts/fibo/SEC/Equities/EquityInstruments/Share.md)

## Annotations

- **label**: custodian
- **definition** (en): financial institution that holds customers' securities for safekeeping
- **adaptedFrom**: https://www.investopedia.com/terms/c/custodian.asp
- **explanatoryNote**: The custodian may hold stocks or other assets in electronic or physical form for mutual funds, individuals, and organizational clients.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
