---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: m b s tranche note
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: An individual note of a tranche.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A Tranche is made up of e.g. $500m in notes and so on. These may be in different notes, with different denominations.
      Analytics that would apply to the Tranche would by implication apply to each slice of the tranche.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/PromissoryNote.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/PromissoryNote
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/MBSTrancheNote
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: m b s tranche note
type: Ontology Class
---

# m b s tranche note

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/MBSTrancheNote>

## Definition

An individual note of a tranche.

## Relationships

- **Subclass of**: [PromissoryNote](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/PromissoryNote.md)

## Annotations

- **label** (en): m b s tranche note
- **definition** (en): An individual note of a tranche.
- **explanatoryNote** (en): A Tranche is made up of e.g. $500m in notes and so on. These may be in different notes, with different denominations. Analytics that would apply to the Tranche would by implication apply to each slice of the tranche.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
