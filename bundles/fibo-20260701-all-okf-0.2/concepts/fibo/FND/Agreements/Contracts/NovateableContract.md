---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: novateable contract
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: contract that may be replaced by another contract, and in that event, extinguishes the rights and obligations in
      effect under the original contract with those in the new agreement
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In general, novation means consensual substitution of a party or obligation in the original contract with a new
      party or obligation in the successor contract. The new party takes on the rights and obligations of the original party.
      The corresponding novation agreement must be signed by the transferor, the transferee, and the counterparty (the other
      contracting party). Novation is frequently used in mergers and acquisitions to replace any outstanding relationships
      or rights and obligations of the organization being subsumed with relationships or obligations of the acquiring entity.
      It is also commonly used with respect to loan rescheduling.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'Novation is different from assignment in the following ways: (1) novation is a consensual transfer of contractual
      rights and obligations, while an assignment can transfer only obligations and does not require the consent of the benefiting
      party, and (2) novation terminates the original contract, but assignment does not.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/TransferableContract.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/TransferableContract
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/NovateableContract
sources:
- id: fibo-source-310cd83e5e
  resource: references/fibo/FND/Agreements/Contracts.rdf
  sha256: 310cd83e5e80f369e3f18c0a064ecf0f9519dae374fd89af25778d1089321ed8
  title: FIBO source FND/Agreements/Contracts.rdf
title: novateable contract
type: Ontology Class
---

# novateable contract

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/NovateableContract>

## Definition

contract that may be replaced by another contract, and in that event, extinguishes the rights and obligations in effect under the original contract with those in the new agreement

## Relationships

- **Subclass of**: [TransferableContract](/concepts/fibo/FND/Agreements/Contracts/TransferableContract.md)

## Annotations

- **label**: novateable contract
- **definition**: contract that may be replaced by another contract, and in that event, extinguishes the rights and obligations in effect under the original contract with those in the new agreement
- **explanatoryNote**: In general, novation means consensual substitution of a party or obligation in the original contract with a new party or obligation in the successor contract. The new party takes on the rights and obligations of the original party. The corresponding novation agreement must be signed by the transferor, the transferee, and the counterparty (the other contracting party). Novation is frequently used in mergers and acquisitions to replace any outstanding relationships or rights and obligations of the organization being subsumed with relationships or obligations of the acquiring entity. It is also commonly used with respect to loan rescheduling.
- **explanatoryNote**: Novation is different from assignment in the following ways: (1) novation is a consensual transfer of contractual rights and obligations, while an assignment can transfer only obligations and does not require the consent of the benefiting party, and (2) novation terminates the original contract, but assignment does not.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
