---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: regulated commodity
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: commodity under the jurisdiction of the regulatory agency, such as the Commodities Futures Trading Commission (CFTF)
      in the United States, which includes any commodity traded in an organized contracts market
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The CFTC polices matters of information and disclosure, fair trading practices, registration of firms and individuals,
      protection of customer funds, record keeping, and maintenance of orderly options and futures markets in the United States.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy
  - filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency
    kind: all_values_from
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/isRegulatedBy
  subclass_of:
  - concept: /concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Commodity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/Commodity
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/RegulatedCommodity
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: regulated commodity
type: Ontology Class
---

# regulated commodity

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/RegulatedCommodity>

## Definition

commodity under the jurisdiction of the regulatory agency, such as the Commodities Futures Trading Commission (CFTF) in the United States, which includes any commodity traded in an organized contracts market

## Relationships

- **Subclass of**: [Commodity](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/Commodity.md)

## Constraints

- **[isGovernedBy](<https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy>)**: some values from of type [Jurisdiction](<https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction>)
- **[isRegulatedBy](<https://www.omg.org/spec/Commons/RegulatoryAgencies/isRegulatedBy>)**: all values from of type [RegulatoryAgency](<https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency>)

## Annotations

- **label**: regulated commodity
- **definition**: commodity under the jurisdiction of the regulatory agency, such as the Commodities Futures Trading Commission (CFTF) in the United States, which includes any commodity traded in an organized contracts market
- **explanatoryNote**: The CFTC polices matters of information and disclosure, fair trading practices, registration of firms and individuals, protection of customer funds, record keeping, and maintenance of orderly options and futures markets in the United States.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
