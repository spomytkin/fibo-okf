---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: bond issuance programme
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a debt issuance programe under which an entity may, from time to time, issue bonds under the terms and conditions
      specified in the base prospectus for that programme
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/BondOffering
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/DebtIssuanceProgramme.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/DebtIssuanceProgramme
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/BondIssuanceProgramme
sources:
- id: fibo-source-560fdfbe3a
  resource: references/fibo/BP/SecuritiesIssuance/DebtIssuance.rdf
  sha256: 560fdfbe3abab0e0bb6f417a8acec1661acf530aeee87d8a033ef11bbf4af57b
  title: FIBO source BP/SecuritiesIssuance/DebtIssuance.rdf
title: bond issuance programme
type: Ontology Class
---

# bond issuance programme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/BondIssuanceProgramme>

## Definition

a debt issuance programe under which an entity may, from time to time, issue bonds under the terms and conditions specified in the base prospectus for that programme

## Relationships

- **Subclass of**: [DebtIssuanceProgramme](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/DebtIssuanceProgramme.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: some values from of type [BondOffering](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/BondOffering.md)

## Annotations

- **label** (en): bond issuance programme
- **definition** (en): a debt issuance programe under which an entity may, from time to time, issue bonds under the terms and conditions specified in the base prospectus for that programme

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
