---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: passport
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: formal identity document, issued by a national government, which certifies the identity and nationality of its
      holder for the purpose of international travel
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/definitionOrigin
    value: https://en.wikipedia.org/wiki/Passport
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The elements of identity contained in all standardized passports include information about the holder, including
      name, date of birth, gender and place of birth.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/PassportNumber
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/IdentityDocument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/IdentityDocument
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Passport
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: passport
type: Ontology Class
---

# passport

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Passport>

## Definition

formal identity document, issued by a national government, which certifies the identity and nationality of its holder for the purpose of international travel

## Relationships

- **Subclass of**: [IdentityDocument](/concepts/fibo/FND/AgentsAndPeople/People/IdentityDocument.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 1 of type [PassportNumber](/concepts/fibo/FND/AgentsAndPeople/People/PassportNumber.md)

## Annotations

- **label**: passport
- **definition**: formal identity document, issued by a national government, which certifies the identity and nationality of its holder for the purpose of international travel
- **definitionOrigin**: https://en.wikipedia.org/wiki/Passport
- **explanatoryNote**: The elements of identity contained in all standardized passports include information about the holder, including name, date of birth, gender and place of birth.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
