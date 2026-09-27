---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: capital lease
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: lease that must be reflected on an organization's balance sheet as an asset and as a corresponding liability
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In the United States, such leases must be reported per Statement 13 of the Financial Accounting Standards Board.
      Generally, this applies to leases where the lessee acquires essentially all of the economic benefits and risks of the
      leased property.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: financial lease
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/Lease.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Lease
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CapitalLease
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: capital lease
type: Ontology Class
---

# capital lease

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CapitalLease>

## Definition

lease that must be reflected on an organization's balance sheet as an asset and as a corresponding liability

## Relationships

- **Subclass of**: [Lease](/concepts/fibo/FBC/DebtAndEquities/Debt/Lease.md)

## Annotations

- **label**: capital lease
- **definition**: lease that must be reflected on an organization's balance sheet as an asset and as a corresponding liability
- **explanatoryNote**: In the United States, such leases must be reported per Statement 13 of the Financial Accounting Standards Board. Generally, this applies to leases where the lessee acquires essentially all of the economic benefits and risks of the leased property.
- **synonym**: financial lease

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
