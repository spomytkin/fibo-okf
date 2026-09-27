---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: significant shareholder
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: party that owns a significant voting stake in an organization that is less than 50 percent but greater than some
      threshold
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that the concept of significance varies depending on the jurisdiction, and particularly with respect to reporting
      requirements. For example, in some cases, three (3) percent ownership of any class or series of shares is considered
      significant, and in others it means more than five or ten percent of the total combined voting power across all classes
      of securities.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateControl/VotingShareholder.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/VotingShareholder
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/SignificantShareholder
sources:
- id: fibo-source-23da6b47b0
  resource: references/fibo/BE/OwnershipAndControl/CorporateControl.rdf
  sha256: 23da6b47b01ef29d26d5aa063b88cb62e44c676204d905b98e96322c216195ab
  title: FIBO source BE/OwnershipAndControl/CorporateControl.rdf
title: significant shareholder
type: Ontology Class
---

# significant shareholder

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/SignificantShareholder>

## Definition

party that owns a significant voting stake in an organization that is less than 50 percent but greater than some threshold

## Relationships

- **Subclass of**: [VotingShareholder](/concepts/fibo/BE/OwnershipAndControl/CorporateControl/VotingShareholder.md)

## Annotations

- **label**: significant shareholder
- **definition**: party that owns a significant voting stake in an organization that is less than 50 percent but greater than some threshold
- **explanatoryNote**: Note that the concept of significance varies depending on the jurisdiction, and particularly with respect to reporting requirements. For example, in some cases, three (3) percent ownership of any class or series of shares is considered significant, and in others it means more than five or ten percent of the total combined voting power across all classes of securities.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
