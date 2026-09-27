---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: debt securitization process
  disjoint_with:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/DebtAuctionProcess.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/DebtAuctionProcess
  - concept: /concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/SecuritiesUnderwritingIssuanceProcess.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/SecuritiesUnderwritingIssuanceProcess
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/SecuritiesIssuanceProcess.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/SecuritiesIssuanceProcess
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/DebtSecuritizationProcess
sources:
- id: fibo-source-560fdfbe3a
  resource: references/fibo/BP/SecuritiesIssuance/DebtIssuance.rdf
  sha256: 560fdfbe3abab0e0bb6f417a8acec1661acf530aeee87d8a033ef11bbf4af57b
  title: FIBO source BP/SecuritiesIssuance/DebtIssuance.rdf
title: debt securitization process
type: Ontology Class
---

# debt securitization process

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/DebtSecuritizationProcess>

## Relationships

- **Subclass of**: [SecuritiesIssuanceProcess](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/SecuritiesIssuanceProcess.md)

## Constraints

- **Disjoint with**: [DebtAuctionProcess](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/DebtAuctionProcess.md)
- **Disjoint with**: [SecuritiesUnderwritingIssuanceProcess](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/SecuritiesUnderwritingIssuanceProcess.md)

## Annotations

- **label** (en): debt securitization process

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
