---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: offshore depositary receipt
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: depositary receipt issued under SEC Regulation S
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This regulation means that the securities are not, and will not be registered with any U.S. securities regulation
      authority. Regulation S shares cannot be held or traded by any 'U.S. person' as defined by SEC Regulation S rules. The
      shares are registered and issued to offshore, non-U.S. residents.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/hasRestriction
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions/RegulationS
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/DepositaryReceipts/SponsoredDepositaryReceipt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/SponsoredDepositaryReceipt
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/OffshoreDepositaryReceipt
sources:
- id: fibo-source-dcb6707b33
  resource: references/fibo/SEC/Equities/DepositaryReceipts.rdf
  sha256: dcb6707b33fd1bafd81ed0f5e71016e204f1eca273f82833bfa9d07319be3b34
  title: FIBO source SEC/Equities/DepositaryReceipts.rdf
title: offshore depositary receipt
type: Ontology Class
---

# offshore depositary receipt

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/OffshoreDepositaryReceipt>

## Definition

depositary receipt issued under SEC Regulation S

## Relationships

- **Subclass of**: [SponsoredDepositaryReceipt](/concepts/fibo/SEC/Equities/DepositaryReceipts/SponsoredDepositaryReceipt.md)

## Constraints

- **[hasRestriction](/concepts/fibo/SEC/Securities/SecuritiesRestrictions/hasRestriction.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions/RegulationS`

## Annotations

- **label** (en): offshore depositary receipt
- **definition** (en): depositary receipt issued under SEC Regulation S
- **explanatoryNote** (en): This regulation means that the securities are not, and will not be registered with any U.S. securities regulation authority. Regulation S shares cannot be held or traded by any 'U.S. person' as defined by SEC Regulation S rules. The shares are registered and issued to offshore, non-U.S. residents.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
