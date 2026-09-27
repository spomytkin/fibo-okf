---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: swap data repository
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial service provider that provides a central facility for swap data reporting and recordkeeping
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: SDR
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.cftc.gov/IndustryOversight/DataRepositories/index.htm
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Swap data repositories ('SDRs') are new entities created by the Dodd-Frank Wall Street Reform and Consumer Protection
      Act ('Dodd-Frank Act') in order to provide a central facility for swap data reporting and recordkeeping. Under the Dodd-
      Frank Act, all swaps, whether cleared or uncleared, are required to be reported to registered SDRs. The Dodd-Frank Act
      added new Section 21 to the Commodity Exchange Act ('CEA'), governing registration and regulation of SDRs and establishing
      registration requirements and core duties and responsibilities for SDRs.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapDataRepository
sources:
- id: fibo-source-d5b3b6ccbc
  resource: references/fibo/DER/DerivativesContracts/Swaps.rdf
  sha256: d5b3b6ccbce15ed5522f2c15fde90c8b79ec7a3de33e9b48a80f97f106582966
  title: FIBO source DER/DerivativesContracts/Swaps.rdf
title: swap data repository
type: Ontology Class
---

# swap data repository

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/Swaps/SwapDataRepository>

## Definition

financial service provider that provides a central facility for swap data reporting and recordkeeping

## Relationships

- **Subclass of**: [FinancialServiceProvider](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/FinancialServiceProvider.md)

## Annotations

- **label**: swap data repository
- **definition**: financial service provider that provides a central facility for swap data reporting and recordkeeping
- **abbreviation**: SDR
- **adaptedFrom**: http://www.cftc.gov/IndustryOversight/DataRepositories/index.htm
- **explanatoryNote**: Swap data repositories ('SDRs') are new entities created by the Dodd-Frank Wall Street Reform and Consumer Protection Act ('Dodd-Frank Act') in order to provide a central facility for swap data reporting and recordkeeping. Under the Dodd- Frank Act, all swaps, whether cleared or uncleared, are required to be reported to registered SDRs. The Dodd-Frank Act added new Section 21 to the Commodity Exchange Act ('CEA'), governing registration and regulation of SDRs and establishing registration requirements and core duties and responsibilities for SDRs.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
