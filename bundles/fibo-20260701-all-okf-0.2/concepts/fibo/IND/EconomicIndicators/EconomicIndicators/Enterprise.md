---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: enterprise
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: functional business entity that produces and/or sells goods or services
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.bls.gov/opub/hom/glossary.htm#E
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: An enterprise (a private firm, government, or nonprofit organization) can consist of a single establishment or
      multiple establishments. All establishments in an enterprise may be classified in one industry (e.g., a chain), or they
      may be classified in different industries (e.g., a conglomerate).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/Establishment
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
    value: Ndda1d11e626c47f5b4400659aa33b3ce
  - filler: https://www.omg.org/spec/Commons/Organizations/LegalPerson
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
  subclass_of:
  - concept: /concepts/fibo/BE/FunctionalEntities/FunctionalEntities/FunctionalBusinessEntity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/FunctionalEntities/FunctionalEntities/FunctionalBusinessEntity
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/InstitutionalUnit.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/InstitutionalUnit
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/Enterprise
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: enterprise
type: Ontology Class
---

# enterprise

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/Enterprise>

## Definition

functional business entity that produces and/or sells goods or services

## Relationships

- **Subclass of**: [FunctionalBusinessEntity](/concepts/fibo/BE/FunctionalEntities/FunctionalEntities/FunctionalBusinessEntity.md)
- **Subclass of**: [InstitutionalUnit](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/InstitutionalUnit.md)

## Constraints

- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: some values from of type [IndustrySectorClassifier](/concepts/fibo/FND/Arrangements/ClassificationSchemes/IndustrySectorClassifier.md)
- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [Establishment](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/Establishment.md)
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from value `Ndda1d11e626c47f5b4400659aa33b3ce`
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from of type [LegalPerson](<https://www.omg.org/spec/Commons/Organizations/LegalPerson>)

## Annotations

- **label**: enterprise
- **definition**: functional business entity that produces and/or sells goods or services
- **adaptedFrom**: http://www.bls.gov/opub/hom/glossary.htm#E
- **explanatoryNote**: An enterprise (a private firm, government, or nonprofit organization) can consist of a single establishment or multiple establishments. All establishments in an enterprise may be classified in one industry (e.g., a chain), or they may be classified in different industries (e.g., a conglomerate).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
