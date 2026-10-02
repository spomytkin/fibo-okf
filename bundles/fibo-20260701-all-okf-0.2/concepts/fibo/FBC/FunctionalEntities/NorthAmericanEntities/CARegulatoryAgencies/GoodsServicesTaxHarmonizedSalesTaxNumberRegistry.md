---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Canada Revenue Agency Goods and Services Tax / Harmonized Sales Tax number registry
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: registry that records and tracks individual GST/HST numbers for the Canada Revenue Agency
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: GST/HST number registry
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Limited public access.
  defined_by:
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/BusinessRegistry
  related_to:
  - concept: /concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/CAGovernmentEntitiesAndJurisdictions/CanadianJurisdiction.md
    predicate: https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/GovernmentEntities/NorthAmericanJurisdiction/CAGovernmentEntitiesAndJurisdictions/CanadianJurisdiction
  - concept: /concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/CanadianBusinessTaxRegistrar.md
    predicate: https://www.omg.org/spec/Commons/Organizations/isManagedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/CanadianBusinessTaxRegistrar
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.canada.ca/en/revenue-agency/services/e-services/e-services-businesses/confirming-a-gst-hst-account-number/terms-conditions-use.html
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/GoodsServicesTaxHarmonizedSalesTaxNumberRegistry
sources:
- id: fibo-source-3a86c5f7dd
  resource: references/fibo/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies.rdf
  sha256: 3a86c5f7dd7acfa3d8ca47686faffd64ac5f85eae9e50730e1337823edbfcda4
  title: FIBO source FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies.rdf
title: Canada Revenue Agency Goods and Services Tax / Harmonized Sales Tax number registry
type: Ontology Individual
---

# Canada Revenue Agency Goods and Services Tax / Harmonized Sales Tax number registry

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/GoodsServicesTaxHarmonizedSalesTaxNumberRegistry>

## Definition

registry that records and tracks individual GST/HST numbers for the Canada Revenue Agency

## Relationships

- **Defined by**: [CARegulatoryAgencies](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies.md)
- **Related to**: [CanadianBusinessTaxRegistrar](/concepts/fibo/FBC/FunctionalEntities/NorthAmericanEntities/CARegulatoryAgencies/CanadianBusinessTaxRegistrar.md)
- **Related to**: [CanadianJurisdiction](/concepts/fibo/BE/GovernmentEntities/NorthAmericanJurisdiction/CAGovernmentEntitiesAndJurisdictions/CanadianJurisdiction.md)
- **See also**: [terms-conditions-use.html](<https://www.canada.ca/en/revenue-agency/services/e-services/e-services-businesses/confirming-a-gst-hst-account-number/terms-conditions-use.html>)

## Annotations

- **label**: Canada Revenue Agency Goods and Services Tax / Harmonized Sales Tax number registry
- **definition**: registry that records and tracks individual GST/HST numbers for the Canada Revenue Agency
- **abbreviation**: GST/HST number registry
- **explanatoryNote**: Limited public access.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
