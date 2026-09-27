---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: unit investment trust
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: investment company which (a) is organized under a trust indenture, contract of custodianship or agency, or similar
      instrument, (b) does not have a board of directors, and (c) issues only redeemable securities, each of which represents
      an undivided interest in a unit of specified securities; but does not include a voting trust
  - predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/definitionOrigin
    value: Section 4, definition of investment companies, Investment Company Act of 1940 as amended and approved as of 3 January
      2012, see https://www.sec.gov/about/laws/ica40.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: UIT
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: unit investment company
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/InvestmentCompany.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/InvestmentCompany
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/UnitInvestmentTrust
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: unit investment trust
type: Ontology Class
---

# unit investment trust

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/UnitInvestmentTrust>

## Definition

investment company which (a) is organized under a trust indenture, contract of custodianship or agency, or similar instrument, (b) does not have a board of directors, and (c) issues only redeemable securities, each of which represents an undivided interest in a unit of specified securities; but does not include a voting trust

## Relationships

- **Subclass of**: [InvestmentCompany](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/InvestmentCompany.md)

## Annotations

- **label**: unit investment trust
- **definition**: investment company which (a) is organized under a trust indenture, contract of custodianship or agency, or similar instrument, (b) does not have a board of directors, and (c) issues only redeemable securities, each of which represents an undivided interest in a unit of specified securities; but does not include a voting trust
- **definitionOrigin**: Section 4, definition of investment companies, Investment Company Act of 1940 as amended and approved as of 3 January 2012, see https://www.sec.gov/about/laws/ica40.pdf
- **abbreviation**: UIT
- **synonym**: unit investment company

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
