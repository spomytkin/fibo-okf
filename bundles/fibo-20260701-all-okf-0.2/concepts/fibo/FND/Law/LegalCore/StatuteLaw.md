---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: statute law
  - predicate: http://www.w3.org/2004/02/skos/core#altLabel
    value: statutory law
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: law enacted by a legislature
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.law.cornell.edu/wex/statute
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In the United States, statutes may also be called acts, such as the Civil Rights Act of 1964 or the Sarbanes-Oxley
      Act. Federal laws must be passed by both houses of Congress, the House of Representative and the Senate, and then usually
      require approval from the president before they can take effect.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Statutes may originate with national, state legislatures or local municipalities. Statutory laws are subordinate
      to the higher constitutional laws of the land.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCore/isInForceIn
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCore/Law.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCore/Law
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCore/StatuteLaw
sources:
- id: fibo-source-31fe191c06
  resource: references/fibo/FND/Law/LegalCore.rdf
  sha256: 31fe191c06f11a104ba752303784bfd17673c9e515a6e3d3ed538b19a5da37e9
  title: FIBO source FND/Law/LegalCore.rdf
title: statute law
type: Ontology Class
---

# statute law

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCore/StatuteLaw>

## Definition

law enacted by a legislature

## Synonyms

- statutory law

## Relationships

- **Subclass of**: [Law](/concepts/fibo/FND/Law/LegalCore/Law.md)

## Constraints

- **[isInForceIn](/concepts/fibo/FND/Law/LegalCore/isInForceIn.md)**: some values from of type [Jurisdiction](<https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction>)

## Annotations

- **label** (en): statute law
- **altLabel**: statutory law
- **definition**: law enacted by a legislature
- **adaptedFrom**: https://www.law.cornell.edu/wex/statute
- **explanatoryNote**: In the United States, statutes may also be called acts, such as the Civil Rights Act of 1964 or the Sarbanes-Oxley Act. Federal laws must be passed by both houses of Congress, the House of Representative and the Senate, and then usually require approval from the president before they can take effect.
- **explanatoryNote**: Statutes may originate with national, state legislatures or local municipalities. Statutory laws are subordinate to the higher constitutional laws of the land.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
