---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: common interest development corporation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: not-for-profit corporation set up under specific state legislation as a business entity for homeowners' associations
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: http://www.dre.ca.gov/files/pdf/re39.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A common interest development is typically a type of housing, composed of individually owned units, such as condominiums,
      townhouses, or single-family homes, that share ownership of common areas, such as swimming pools, landscaping, and parking.
      Common interest developments (also known as community interest developments or CIDs) are managed by homeowners' associations.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/LegalEntities/CorporateBodies/NotForProfitCorporation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/NotForProfitCorporation
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/CommonInterestDevelopmentCorporation
sources:
- id: fibo-source-6fa4a51dba
  resource: references/fibo/BE/LegalEntities/CorporateBodies.rdf
  sha256: 6fa4a51dba5b2409b4becae9f17299d91b3fd0da0b7a4439f6c3888b6f1dd363
  title: FIBO source BE/LegalEntities/CorporateBodies.rdf
title: common interest development corporation
type: Ontology Class
---

# common interest development corporation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/CommonInterestDevelopmentCorporation>

## Definition

not-for-profit corporation set up under specific state legislation as a business entity for homeowners' associations

## Relationships

- **Subclass of**: [NotForProfitCorporation](/concepts/fibo/BE/LegalEntities/CorporateBodies/NotForProfitCorporation.md)

## Annotations

- **label**: common interest development corporation
- **definition**: not-for-profit corporation set up under specific state legislation as a business entity for homeowners' associations
- **example**: http://www.dre.ca.gov/files/pdf/re39.pdf
- **explanatoryNote**: A common interest development is typically a type of housing, composed of individually owned units, such as condominiums, townhouses, or single-family homes, that share ownership of common areas, such as swimming pools, landscaping, and parking. Common interest developments (also known as community interest developments or CIDs) are managed by homeowners' associations.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
