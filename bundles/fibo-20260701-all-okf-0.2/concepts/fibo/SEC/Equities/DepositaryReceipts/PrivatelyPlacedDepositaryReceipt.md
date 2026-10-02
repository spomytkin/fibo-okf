---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: privately placed depositary receipt
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: depositary receipt that represents shares in a private placement under the SEC Rule 144-A
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Some foreign companies will set up an ADR program under SEC Rule 144-A. This provision makes the issuance of shares
      a private placement. Shares of companies registered under Rule 144-A are restricted stock and may only be issued to
      or traded by qualified institutional buyers (QIBs). U.S. public shareholders are generally not permitted to invest in
      these ADR programs, and most are held exclusively through the Depository Trust & Clearing Corporation, so there is often
      very little information on these companies.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/hasRestriction
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions/Rule144A
  subclass_of:
  - concept: /concepts/fibo/SEC/Equities/DepositaryReceipts/SponsoredDepositaryReceipt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/SponsoredDepositaryReceipt
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/PrivatelyPlacedDepositaryReceipt
sources:
- id: fibo-source-dcb6707b33
  resource: references/fibo/SEC/Equities/DepositaryReceipts.rdf
  sha256: dcb6707b33fd1bafd81ed0f5e71016e204f1eca273f82833bfa9d07319be3b34
  title: FIBO source SEC/Equities/DepositaryReceipts.rdf
title: privately placed depositary receipt
type: Ontology Class
---

# privately placed depositary receipt

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Equities/DepositaryReceipts/PrivatelyPlacedDepositaryReceipt>

## Definition

depositary receipt that represents shares in a private placement under the SEC Rule 144-A

## Relationships

- **Subclass of**: [SponsoredDepositaryReceipt](/concepts/fibo/SEC/Equities/DepositaryReceipts/SponsoredDepositaryReceipt.md)

## Constraints

- **[hasRestriction](/concepts/fibo/SEC/Securities/SecuritiesRestrictions/hasRestriction.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/NorthAmericanSecurities/USSecuritiesRestrictions/Rule144A`

## Annotations

- **label** (en): privately placed depositary receipt
- **definition** (en): depositary receipt that represents shares in a private placement under the SEC Rule 144-A
- **explanatoryNote** (en): Some foreign companies will set up an ADR program under SEC Rule 144-A. This provision makes the issuance of shares a private placement. Shares of companies registered under Rule 144-A are restricted stock and may only be issued to or traded by qualified institutional buyers (QIBs). U.S. public shareholders are generally not permitted to invest in these ADR programs, and most are held exclusively through the Depository Trust & Clearing Corporation, so there is often very little information on these companies.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
