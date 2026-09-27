---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: instrument of incorporation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: memorandum and articles of association by which some legal entity is established
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This may be the issuance of shares, the existence of some agreement, guaranties and so on.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCore/Constitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCore/Constitution
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/InstrumentOfIncorporation
sources:
- id: fibo-source-6fa4a51dba
  resource: references/fibo/BE/LegalEntities/CorporateBodies.rdf
  sha256: 6fa4a51dba5b2409b4becae9f17299d91b3fd0da0b7a4439f6c3888b6f1dd363
  title: FIBO source BE/LegalEntities/CorporateBodies.rdf
title: instrument of incorporation
type: Ontology Class
---

# instrument of incorporation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/CorporateBodies/InstrumentOfIncorporation>

## Definition

memorandum and articles of association by which some legal entity is established

## Relationships

- **Subclass of**: [Constitution](/concepts/fibo/FND/Law/LegalCore/Constitution.md)

## Constraints

- **[isGovernedBy](<https://www.omg.org/spec/Commons/RegulatoryAgencies/isGovernedBy>)**: exact qualified cardinality 1 of type [Jurisdiction](<https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction>)

## Annotations

- **label**: instrument of incorporation
- **definition**: memorandum and articles of association by which some legal entity is established
- **explanatoryNote**: This may be the issuance of shares, the existence of some agreement, guaranties and so on.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
