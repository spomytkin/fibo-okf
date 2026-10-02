---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: merchant category code scheme
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: scheme defining a set of codes for classifying merchant services
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 18245:2003 Retail financial services - Merchant category codes
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: ISO 18245 provides a set of merchant category codes that are used internationally. Some countries, regional governments,
      banks, and other large organizations extend the basic codes with custom additions to fit business needs.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/MerchantCategoryCode
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/defines
  subclass_of:
  - concept: /concepts/fibo/FND/Arrangements/ClassificationSchemes/IndustrySectorClassificationScheme.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/ClassificationSchemes/IndustrySectorClassificationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/MerchantCategoryCodeScheme
sources:
- id: fibo-source-1a60609b6a
  resource: references/fibo/BE/FunctionalEntities/FunctionalEntities.rdf
  sha256: 1a60609b6ad170e85bb9424d06c7d8f740d0c98492e22a8c0c9e2e285ec47b5a
  title: FIBO source BE/FunctionalEntities/FunctionalEntities.rdf
title: merchant category code scheme
type: Ontology Class
---

# merchant category code scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/MerchantCategoryCodeScheme>

## Definition

scheme defining a set of codes for classifying merchant services

## Relationships

- **Subclass of**: [IndustrySectorClassificationScheme](/concepts/fibo/FND/Arrangements/ClassificationSchemes/IndustrySectorClassificationScheme.md)

## Constraints

- **[defines](<https://www.omg.org/spec/Commons/Designators/defines>)**: some values from of type [MerchantCategoryCode](/concepts/fibo/BE/FunctionalEntities/FunctionalEntities/MerchantCategoryCode.md)

## Annotations

- **label**: merchant category code scheme
- **definition**: scheme defining a set of codes for classifying merchant services
- **adaptedFrom**: ISO 18245:2003 Retail financial services - Merchant category codes
- **explanatoryNote**: ISO 18245 provides a set of merchant category codes that are used internationally. Some countries, regional governments, banks, and other large organizations extend the basic codes with custom additions to fit business needs.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
