---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: chief executive officer
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: top corporate officer responsible for an organization's overall operations and performance
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: CEO
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: He or she is the leader of the firm, serves as the main link between the board of directors (the board) and the
      firm's various parts or levels, and is held solely responsible for the firm's success or failure. One of the major duties
      of a CEO is to maintain and implement corporate policy, as established by the board. Also called President or managing
      director, he or she may also be the chairman (or chairperson) of the board.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/manages
    value: Nf0e4c4dd238844efb03ffc53ebd37164
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives/CorporateOfficer.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/CorporateOfficer
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives/ExecutiveBoardMember.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/ExecutiveBoardMember
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives/PrincipalParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/PrincipalParty
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/ChiefExecutiveOfficer
sources:
- id: fibo-source-27c89de7b6
  resource: references/fibo/BE/OwnershipAndControl/Executives.rdf
  sha256: 27c89de7b6ec909d26a0a73d1d2b7cbaadf425eb5e6a488f681cc3eba80f91ca
  title: FIBO source BE/OwnershipAndControl/Executives.rdf
title: chief executive officer
type: Ontology Class
---

# chief executive officer

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/ChiefExecutiveOfficer>

## Definition

top corporate officer responsible for an organization's overall operations and performance

## Relationships

- **Subclass of**: [CorporateOfficer](/concepts/fibo/BE/OwnershipAndControl/Executives/CorporateOfficer.md)
- **Subclass of**: [ExecutiveBoardMember](/concepts/fibo/BE/OwnershipAndControl/Executives/ExecutiveBoardMember.md)
- **Subclass of**: [PrincipalParty](/concepts/fibo/BE/OwnershipAndControl/Executives/PrincipalParty.md)

## Constraints

- **[manages](<https://www.omg.org/spec/Commons/Organizations/manages>)**: some values from value `Nf0e4c4dd238844efb03ffc53ebd37164`

## Annotations

- **label**: chief executive officer
- **definition**: top corporate officer responsible for an organization's overall operations and performance
- **abbreviation**: CEO
- **explanatoryNote**: He or she is the leader of the firm, serves as the main link between the board of directors (the board) and the firm's various parts or levels, and is held solely responsible for the firm's success or failure. One of the major duties of a CEO is to maintain and implement corporate policy, as established by the board. Also called President or managing director, he or she may also be the chairman (or chairperson) of the board.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
