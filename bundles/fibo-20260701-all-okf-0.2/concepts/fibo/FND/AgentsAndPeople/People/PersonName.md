---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: person name
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: designation by which someone is known in some context
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/TextDatatype/Text
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasFullLegalName
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/TextDatatype/Text
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasNamePrefix
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/TextDatatype/Text
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasNameSuffix
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/TextDatatype/Text
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasSurname
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Person
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/isNameOf
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/ContextualDesignators/ContextualName
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/PersonName
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: person name
type: Ontology Class
---

# person name

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/PersonName>

## Definition

designation by which someone is known in some context

## Relationships

- **Subclass of**: [ContextualName](<https://www.omg.org/spec/Commons/ContextualDesignators/ContextualName>)

## Constraints

- **[hasFullLegalName](/concepts/fibo/FND/AgentsAndPeople/People/hasFullLegalName.md)**: min qualified cardinality 0 of type [Text](<https://www.omg.org/spec/Commons/TextDatatype/Text>)
- **[hasNamePrefix](/concepts/fibo/FND/AgentsAndPeople/People/hasNamePrefix.md)**: min qualified cardinality 0 of type [Text](<https://www.omg.org/spec/Commons/TextDatatype/Text>)
- **[hasNameSuffix](/concepts/fibo/FND/AgentsAndPeople/People/hasNameSuffix.md)**: min qualified cardinality 0 of type [Text](<https://www.omg.org/spec/Commons/TextDatatype/Text>)
- **[hasSurname](/concepts/fibo/FND/AgentsAndPeople/People/hasSurname.md)**: min qualified cardinality 0 of type [Text](<https://www.omg.org/spec/Commons/TextDatatype/Text>)
- **[isNameOf](<https://www.omg.org/spec/Commons/Designators/isNameOf>)**: min qualified cardinality 0 of type [Person](/concepts/fibo/FND/AgentsAndPeople/People/Person.md)

## Annotations

- **label**: person name
- **definition**: designation by which someone is known in some context

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
