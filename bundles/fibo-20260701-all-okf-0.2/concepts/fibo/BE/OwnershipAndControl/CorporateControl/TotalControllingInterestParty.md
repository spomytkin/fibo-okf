---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: total controlling interest party
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: voting shareholder that owns 100 percent of the voting shares in some legal entity
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: By virtue of holding 100 percent of the share ownership, the total controlling interest company also holds 100
      percent of the controlling equity, if there is a difference. Therefore, it is both a total owner and a total controlling
      party.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: parent company
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties/TotalOwner.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/TotalOwner
  - concept: /concepts/fibo/BE/OwnershipAndControl/CorporateControl/SignificantShareholder.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/SignificantShareholder
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/TotalControllingInterestParty
sources:
- id: fibo-source-23da6b47b0
  resource: references/fibo/BE/OwnershipAndControl/CorporateControl.rdf
  sha256: 23da6b47b01ef29d26d5aa063b88cb62e44c676204d905b98e96322c216195ab
  title: FIBO source BE/OwnershipAndControl/CorporateControl.rdf
title: total controlling interest party
type: Ontology Class
---

# total controlling interest party

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/CorporateControl/TotalControllingInterestParty>

## Definition

voting shareholder that owns 100 percent of the voting shares in some legal entity

## Relationships

- **Subclass of**: [TotalOwner](/concepts/fibo/BE/OwnershipAndControl/ControlParties/TotalOwner.md)
- **Subclass of**: [SignificantShareholder](/concepts/fibo/BE/OwnershipAndControl/CorporateControl/SignificantShareholder.md)

## Annotations

- **label**: total controlling interest party
- **definition**: voting shareholder that owns 100 percent of the voting shares in some legal entity
- **explanatoryNote**: By virtue of holding 100 percent of the share ownership, the total controlling interest company also holds 100 percent of the controlling equity, if there is a difference. Therefore, it is both a total owner and a total controlling party.
- **synonym**: parent company

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
