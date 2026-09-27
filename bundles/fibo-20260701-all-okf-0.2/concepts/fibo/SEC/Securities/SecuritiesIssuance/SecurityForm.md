---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: security form
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: nature of the proof of ownership of a security
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Securities are typically issued in one of two forms, registered or bearer. Most securities issued today are in
      registered form, which enables the issuing firm or registrar to keep records of a security's owner and mail them any
      dividend, coupon, or other payments. Registered securities may be issued in book entry (digital only) or certificate
      (physical) form, but most today are entirely digital.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/FinancialAsset
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/exemplifies
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractDocument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractDocument
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/SecurityForm
sources:
- id: fibo-source-7b3088e831
  resource: references/fibo/SEC/Securities/SecuritiesIssuance.rdf
  sha256: 7b3088e8315beedb43222e345522bb546f87fbbd6850833103c9ba84ea1d7ac0
  title: FIBO source SEC/Securities/SecuritiesIssuance.rdf
title: security form
type: Ontology Class
---

# security form

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/SecurityForm>

## Definition

nature of the proof of ownership of a security

## Relationships

- **Subclass of**: [ContractDocument](/concepts/fibo/FND/Agreements/Contracts/ContractDocument.md)

## Constraints

- **[exemplifies](/concepts/fibo/FND/Relations/Relations/exemplifies.md)**: some values from of type [FinancialAsset](/concepts/fibo/FND/OwnershipAndControl/Ownership/FinancialAsset.md)
- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)

## Annotations

- **label**: security form
- **definition**: nature of the proof of ownership of a security
- **explanatoryNote**: Securities are typically issued in one of two forms, registered or bearer. Most securities issued today are in registered form, which enables the issuing firm or registrar to keep records of a security's owner and mail them any dividend, coupon, or other payments. Registered securities may be issued in book entry (digital only) or certificate (physical) form, but most today are entirely digital.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
