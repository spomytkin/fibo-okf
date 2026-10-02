---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: licensor
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a party who grants a license
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Barron's Dictionary of Business and Economics Terms, Fifth Edition, 2012
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: http://www.w3.org/2002/07/owl#Thing
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/licenses
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/License
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/issues
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy
    value: N75718cdfb7e748d497a282e25a07efe2
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/Licensor
sources:
- id: fibo-source-544b6eb4c7
  resource: references/fibo/FND/Law/LegalCapacity.rdf
  sha256: 544b6eb4c7d0acd6efdeb794a9af17ec89bec5145b178192396defaa50bbef22
  title: FIBO source FND/Law/LegalCapacity.rdf
title: licensor
type: Ontology Class
---

# licensor

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/Licensor>

## Definition

a party who grants a license

## Relationships

- **Subclass of**: [PartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/PartyRole>)

## Constraints

- **[licenses](/concepts/fibo/FND/Law/LegalCapacity/licenses.md)**: some values from of type [Thing](<http://www.w3.org/2002/07/owl#Thing>)
- **[issues](/concepts/fibo/FND/Relations/Relations/issues.md)**: some values from of type [License](/concepts/fibo/FND/Law/LegalCapacity/License.md)
- **[isPlayedBy](<https://www.omg.org/spec/Commons/RolesAndCompositions/isPlayedBy>)**: some values from value `N75718cdfb7e748d497a282e25a07efe2`

## Annotations

- **label**: licensor
- **definition**: a party who grants a license
- **adaptedFrom**: Barron's Dictionary of Business and Economics Terms, Fifth Edition, 2012

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
