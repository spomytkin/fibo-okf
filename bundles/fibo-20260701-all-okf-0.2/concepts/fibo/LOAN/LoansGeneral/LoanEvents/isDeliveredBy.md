---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is delivered by
  domain:
  - concept: /concepts/fibo/LOAN/LoansGeneral/LoanEvents/CourtJudgment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanEvents/CourtJudgment
  range:
  - concept: /concepts/fibo/FND/Law/LegalCore/CourtOfLaw.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCore/CourtOfLaw
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanEvents/isDeliveredBy
sources:
- id: fibo-source-48fe43dc99
  resource: references/fibo/LOAN/LoansGeneral/LoanEvents.rdf
  sha256: 48fe43dc99b1d7ca56ee712ff80baad56b5ac6abd1e4cb8ac5342e7bdee88e6e
  title: FIBO source LOAN/LoansGeneral/LoanEvents.rdf
title: is delivered by
type: Ontology Property
---

# is delivered by

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoanEvents/isDeliveredBy>

## Relationships

- **Domain**: [CourtJudgment](/concepts/fibo/LOAN/LoansGeneral/LoanEvents/CourtJudgment.md)
- **Range**: [CourtOfLaw](/concepts/fibo/FND/Law/LegalCore/CourtOfLaw.md)

## Annotations

- **label** (en): is delivered by

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
