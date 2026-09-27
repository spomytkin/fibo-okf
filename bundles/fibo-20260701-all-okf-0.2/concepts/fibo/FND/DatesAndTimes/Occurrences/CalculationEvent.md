---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: calculation event
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: kind of event that is either scheduled or triggered by something, such as a related financial event, that causes
      a calculation to be performed
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: A calculation event may be prescriptive, that occurs within a specified period, or ad hoc.
  - predicate: http://www.w3.org/2004/02/skos/core#note
    value: A calculation event related to a debt instrument might be a rate reset event, calculation of interest subsequent
      to a rate change, an amortization calculation, calculation of interest and/or recalculation of principal due to a late
      payment, etc. A calculation event related to an investment might involve the adjustment of the number of shares owned,
      such as a redemption or dividend related event.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/Calculation
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/classifies
  subclass_of:
  - concept: /concepts/fibo/FND/DatesAndTimes/Occurrences/OccurrenceKind.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/OccurrenceKind
resource: https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/CalculationEvent
sources:
- id: fibo-source-406cc745cc
  resource: references/fibo/FND/DatesAndTimes/Occurrences.rdf
  sha256: 406cc745cc7d791f79c22e8e117f06460564cc81d90a6349ea20adeb5766198c
  title: FIBO source FND/DatesAndTimes/Occurrences.rdf
title: calculation event
type: Ontology Class
---

# calculation event

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/DatesAndTimes/Occurrences/CalculationEvent>

## Definition

kind of event that is either scheduled or triggered by something, such as a related financial event, that causes a calculation to be performed

## Relationships

- **Subclass of**: [OccurrenceKind](/concepts/fibo/FND/DatesAndTimes/Occurrences/OccurrenceKind.md)

## Constraints

- **[classifies](<https://www.omg.org/spec/Commons/Classifiers/classifies>)**: some values from of type [Calculation](/concepts/fibo/FND/DatesAndTimes/Occurrences/Calculation.md)

## Annotations

- **label**: calculation event
- **definition**: kind of event that is either scheduled or triggered by something, such as a related financial event, that causes a calculation to be performed
- **note**: A calculation event may be prescriptive, that occurs within a specified period, or ad hoc.
- **note**: A calculation event related to a debt instrument might be a rate reset event, calculation of interest subsequent to a rate change, an amortization calculation, calculation of interest and/or recalculation of principal due to a late payment, etc. A calculation event related to an investment might involve the adjustment of the number of shares owned, such as a redemption or dividend related event.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
