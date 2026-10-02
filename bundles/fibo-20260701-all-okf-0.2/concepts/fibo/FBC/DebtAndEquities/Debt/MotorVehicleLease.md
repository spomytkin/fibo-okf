---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: motor vehicle lease
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: lease of a motor vehicle for a fixed period of time at an agreed amount of money
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Motor vehicle leasing is commonly offered by dealers as an alternative to a vehicle purchase but is widely used
      by businesses as a method of acquiring (or having the use of) vehicles for business use, without the usually needed
      cash outlay. The key difference in a lease is that after the primary term (usually 2, 3 or 4 years) the vehicle has
      to either be returned to the leasing company or purchased for the residual value.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt/Lease.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Lease
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/MotorVehicleLease
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: motor vehicle lease
type: Ontology Class
---

# motor vehicle lease

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/MotorVehicleLease>

## Definition

lease of a motor vehicle for a fixed period of time at an agreed amount of money

## Relationships

- **Subclass of**: [Lease](/concepts/fibo/FBC/DebtAndEquities/Debt/Lease.md)

## Annotations

- **label**: motor vehicle lease
- **definition**: lease of a motor vehicle for a fixed period of time at an agreed amount of money
- **explanatoryNote**: Motor vehicle leasing is commonly offered by dealers as an alternative to a vehicle purchase but is widely used by businesses as a method of acquiring (or having the use of) vehicles for business use, without the usually needed cash outlay. The key difference in a lease is that after the primary term (usually 2, 3 or 4 years) the vehicle has to either be returned to the leasing company or purchased for the residual value.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
