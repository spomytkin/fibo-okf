---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: has guarantor party
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates a party that guarantees, endorses, or provides indemnity for some obligation on its behalf
  domain:
  - concept: /concepts/fibo/BE/OwnershipAndControl/ControlParties/ControlledParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/ControlParties/ControlledParty
  inverse_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Guaranty/isGuarantorOf.md
    predicate: http://www.w3.org/2002/07/owl#inverseOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/isGuarantorOf
  range:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Guaranty/Guarantor.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/Guarantor
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/OwnershipAndControl/Control/hasControllingParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Control/hasControllingParty
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/hasGuarantorParty
sources:
- id: fibo-source-a6bc9592ee
  resource: references/fibo/FBC/DebtAndEquities/Guaranty.rdf
  sha256: a6bc9592eeebb061e99b2dc168751d4b3612dbcc32c86c50959e17011e4247b0
  title: FIBO source FBC/DebtAndEquities/Guaranty.rdf
title: has guarantor party
type: Ontology Property
---

# has guarantor party

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/hasGuarantorParty>

## Definition

indicates a party that guarantees, endorses, or provides indemnity for some obligation on its behalf

## Relationships

- **Domain**: [ControlledParty](/concepts/fibo/BE/OwnershipAndControl/ControlParties/ControlledParty.md)
- **Inverse of**: [isGuarantorOf](/concepts/fibo/FBC/DebtAndEquities/Guaranty/isGuarantorOf.md)
- **Range**: [Guarantor](/concepts/fibo/FBC/DebtAndEquities/Guaranty/Guarantor.md)
- **Subproperty of**: [hasControllingParty](/concepts/fibo/FND/OwnershipAndControl/Control/hasControllingParty.md)

## Annotations

- **label**: has guarantor party
- **definition**: indicates a party that guarantees, endorses, or provides indemnity for some obligation on its behalf

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
