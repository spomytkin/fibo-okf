---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: contact record
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: record about a party in a specific communicative or liaison role
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Contact records may include attributes such as name, role, communication channel, and affiliation, They may be
      found in registries, schemas, systems such as those designed for customer relationship management (CRM), enterprise
      resource planning (ERP), health information, legal and regulatory compliance and others, as well as personal address
      books, to support communications, coordination, support, or compliance.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Parties/Parties/PartyRoleIdentifier
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/Contact
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/denotes
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Documents/Record
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/ContactRecord
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
title: contact record
type: Ontology Class
---

# contact record

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/ContactRecord>

## Definition

record about a party in a specific communicative or liaison role

## Relationships

- **Subclass of**: [Record](<https://www.omg.org/spec/Commons/Documents/Record>)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 1 of type [PartyRoleIdentifier](/concepts/fibo/FND/Parties/Parties/PartyRoleIdentifier.md)
- **[denotes](<https://www.omg.org/spec/Commons/Designators/denotes>)**: exact qualified cardinality 1 of type [Contact](/concepts/fibo/FND/AgentsAndPeople/People/Contact.md)

## Annotations

- **label**: contact record
- **definition**: record about a party in a specific communicative or liaison role
- **explanatoryNote**: Contact records may include attributes such as name, role, communication channel, and affiliation, They may be found in registries, schemas, systems such as those designed for customer relationship management (CRM), enterprise resource planning (ERP), health information, legal and regulatory compliance and others, as well as personal address books, to support communications, coordination, support, or compliance.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
