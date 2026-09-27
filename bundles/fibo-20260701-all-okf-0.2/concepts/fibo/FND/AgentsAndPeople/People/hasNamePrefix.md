---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has name prefix
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a character or sequence of characters, preceding a person's name, that provides additional information
      about the person, such as a form of address representing a title, honorific, or military rank
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/TextDatatype/hasTextValue
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasNamePrefix
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: has name prefix
type: Ontology Property
---

# has name prefix

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/hasNamePrefix>

## Definition

indicates a character or sequence of characters, preceding a person's name, that provides additional information about the person, such as a form of address representing a title, honorific, or military rank

## Relationships

- **Subproperty of**: [hasTextValue](<https://www.omg.org/spec/Commons/TextDatatype/hasTextValue>)

## Annotations

- **label**: has name prefix
- **definition**: indicates a character or sequence of characters, preceding a person's name, that provides additional information about the person, such as a form of address representing a title, honorific, or military rank

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
