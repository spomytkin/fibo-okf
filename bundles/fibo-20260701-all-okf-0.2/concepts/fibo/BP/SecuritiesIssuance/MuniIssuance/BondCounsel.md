---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: bond counsel
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/DebtUnderwritingIssuanceProcess
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/isBondCounsel
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/ContractThirdParty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/ContractThirdParty
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/BondCounsel
sources:
- id: fibo-source-1c106070e5
  resource: references/fibo/BP/SecuritiesIssuance/MuniIssuance.rdf
  sha256: 1c106070e511dce04ec6498cc5a5df3f6dba9e882ef25649d5ada289a93e628f
  title: FIBO source BP/SecuritiesIssuance/MuniIssuance.rdf
title: bond counsel
type: Ontology Class
---

# bond counsel

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/BondCounsel>

## Relationships

- **Subclass of**: [ContractThirdParty](/concepts/fibo/FND/Agreements/Contracts/ContractThirdParty.md)

## Constraints

- **[isBondCounsel](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/isBondCounsel.md)**: some values from of type [DebtUnderwritingIssuanceProcess](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/DebtUnderwritingIssuanceProcess.md)

## Annotations

- **label** (en): bond counsel

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
