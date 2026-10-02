---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: license
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: grant of permission needed to do something
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Barron's Dictionary of Business and Economics Terms, Fifth Edition, 2012
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that in some cases, a license may also be considered an agreement or contract, depending on the specifics
      of the license and jurisdiction.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LegalCapacity
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/confers
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/Licensor
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isIssuedBy
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/Licensee
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/PartiesAndSituations/holdsDuring
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Documents/LegalDocument
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/License
sources:
- id: fibo-source-544b6eb4c7
  resource: references/fibo/FND/Law/LegalCapacity.rdf
  sha256: 544b6eb4c7d0acd6efdeb794a9af17ec89bec5145b178192396defaa50bbef22
  title: FIBO source FND/Law/LegalCapacity.rdf
title: license
type: Ontology Class
---

# license

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/License>

## Definition

grant of permission needed to do something

## Relationships

- **Subclass of**: [LegalDocument](<https://www.omg.org/spec/Commons/Documents/LegalDocument>)

## Constraints

- **[confers](/concepts/fibo/FND/Relations/Relations/confers.md)**: some values from of type [LegalCapacity](/concepts/fibo/FND/Law/LegalCapacity/LegalCapacity.md)
- **[isIssuedBy](/concepts/fibo/FND/Relations/Relations/isIssuedBy.md)**: some values from of type [Licensor](/concepts/fibo/FND/Law/LegalCapacity/Licensor.md)
- **[hasPartyRole](<https://www.omg.org/spec/Commons/PartiesAndSituations/hasPartyRole>)**: some values from of type [Licensee](/concepts/fibo/FND/Law/LegalCapacity/Licensee.md)
- **[holdsDuring](<https://www.omg.org/spec/Commons/PartiesAndSituations/holdsDuring>)**: exact qualified cardinality 1 of type [DatePeriod](<https://www.omg.org/spec/Commons/DatesAndTimes/DatePeriod>)

## Annotations

- **label**: license
- **definition**: grant of permission needed to do something
- **adaptedFrom**: Barron's Dictionary of Business and Economics Terms, Fifth Edition, 2012
- **explanatoryNote**: Note that in some cases, a license may also be considered an agreement or contract, depending on the specifics of the license and jurisdiction.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
