---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: birth certificate
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: an original document certifying the circumstances of the birth, or a certified copy of or representation of the
      ensuing registration of that birth
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://en.wikipedia.org/wiki/Birth_certificate
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A birth certificate is a vital record that documents the birth of a child. Depending on the jurisdiction, a record
      of birth might or might not contain verification of the event by such as a midwife or doctor.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: certificate of live birth
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/PlaceOfBirth
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isEvidenceFor
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/BirthCertificateIdentifier
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy
  subclass_of:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/IdentityDocument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/IdentityDocument
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Documents/Certificate
resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/BirthCertificate
sources:
- id: fibo-source-ad5313f34d
  resource: references/fibo/FND/AgentsAndPeople/People.rdf
  sha256: ad5313f34d5a14c86455f952c2daeb486e6560ce3168a66d7e1c262b492c22ae
  title: FIBO source FND/AgentsAndPeople/People.rdf
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: birth certificate
type: Ontology Class
---

# birth certificate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/BirthCertificate>

## Definition

an original document certifying the circumstances of the birth, or a certified copy of or representation of the ensuing registration of that birth

## Relationships

- **Subclass of**: [IdentityDocument](/concepts/fibo/FND/AgentsAndPeople/People/IdentityDocument.md)
- **Subclass of**: [Certificate](<https://www.omg.org/spec/Commons/Documents/Certificate>)

## Constraints

- **[isEvidenceFor](/concepts/fibo/FND/Agreements/Contracts/isEvidenceFor.md)**: exact qualified cardinality 1 of type [PlaceOfBirth](/concepts/fibo/FND/AgentsAndPeople/People/PlaceOfBirth.md)
- **[isIdentifiedBy](<https://www.omg.org/spec/Commons/Identifiers/isIdentifiedBy>)**: exact qualified cardinality 1 of type [BirthCertificateIdentifier](/concepts/fibo/FND/AgentsAndPeople/People/BirthCertificateIdentifier.md)

## Annotations

- **label**: birth certificate
- **definition**: an original document certifying the circumstances of the birth, or a certified copy of or representation of the ensuing registration of that birth
- **adaptedFrom**: http://en.wikipedia.org/wiki/Birth_certificate
- **explanatoryNote**: A birth certificate is a vital record that documents the birth of a child. Depending on the jurisdiction, a record of birth might or might not contain verification of the event by such as a midwife or doctor.
- **synonym**: certificate of live birth

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
