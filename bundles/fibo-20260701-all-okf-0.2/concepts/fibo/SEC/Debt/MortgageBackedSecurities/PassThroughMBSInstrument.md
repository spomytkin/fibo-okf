---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: pass through m b s instrument
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: A security in which the cash flows from the underlying asset pool are passed through to the investor by way of
      redemption payments.
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/TranchedMBSInstrument.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/TranchedMBSInstrument
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/PassThroughMBSInstrumentNote
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/hasNote
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/MortgageBackedSecurities/MortgageBackedSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/MortgageBackedSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/PassThroughMBSInstrument
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
- id: fibo-source-025d7e8955
  resource: references/fibo/SEC/Debt/MortgageBackedSecurities.rdf
  sha256: 025d7e89558a319cbd2b60f6a11ca228190a5137c59ed5b5bf34878c5f976f60
  title: FIBO source SEC/Debt/MortgageBackedSecurities.rdf
title: pass through m b s instrument
type: Ontology Class
---

# pass through m b s instrument

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/PassThroughMBSInstrument>

## Definition

A security in which the cash flows from the underlying asset pool are passed through to the investor by way of redemption payments.

## Relationships

- **Subclass of**: [MortgageBackedSecurity](/concepts/fibo/SEC/Debt/MortgageBackedSecurities/MortgageBackedSecurity.md)

## Constraints

- **Disjoint with**: [TranchedMBSInstrument](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/TranchedMBSInstrument.md)
- **[hasNote](/concepts/fibo/SEC/Debt/MortgageBackedSecurities/hasNote.md)**: some values from of type [PassThroughMBSInstrumentNote](/concepts/fibo/SEC/Debt/MortgageBackedSecurities/PassThroughMBSInstrumentNote.md)

## Annotations

- **label** (en): pass through m b s instrument
- **definition** (en): A security in which the cash flows from the underlying asset pool are passed through to the investor by way of redemption payments.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
