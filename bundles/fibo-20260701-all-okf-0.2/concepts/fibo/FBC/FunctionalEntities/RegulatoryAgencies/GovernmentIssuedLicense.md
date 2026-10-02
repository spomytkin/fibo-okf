---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: government-issued license
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: grant of permission needed to legally perform some task, provide some service, exercise a certain privilege, or
      pursue some business or occupation
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Barron's Dictionary of Business and Economics Terms, Fifth Edition, 2012
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isIssuedBy
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/License.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/License
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/RegulatoryAgencies/GovernmentIssuedLicense
sources:
- id: fibo-source-ef717d20cc
  resource: references/fibo/FBC/FunctionalEntities/RegulatoryAgencies.rdf
  sha256: ef717d20cc3804b8cc9643a625bf716211db11cc374a524b54dd5ce7e70bf1db
  title: FIBO source FBC/FunctionalEntities/RegulatoryAgencies.rdf
title: government-issued license
type: Ontology Class
---

# government-issued license

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/RegulatoryAgencies/GovernmentIssuedLicense>

## Definition

grant of permission needed to legally perform some task, provide some service, exercise a certain privilege, or pursue some business or occupation

## Relationships

- **Subclass of**: [License](/concepts/fibo/FND/Law/LegalCapacity/License.md)

## Constraints

- **[isIssuedBy](/concepts/fibo/FND/Relations/Relations/isIssuedBy.md)**: some values from of type [RegulatoryAgency](<https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency>)

## Annotations

- **label**: government-issued license
- **definition**: grant of permission needed to legally perform some task, provide some service, exercise a certain privilege, or pursue some business or occupation
- **adaptedFrom**: Barron's Dictionary of Business and Economics Terms, Fifth Edition, 2012

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
