---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: delivery point code
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: specific set of digits between 00 and 99 assigned to a delivery point
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: When combined with the ZIP + 4 code, the delivery point code provides a unique identifier for every deliverable
      address served by the USPS. The delivery point digits are almost never printed on mail in human-readable form; instead
      they are encoded in the POSTNET delivery point barcode (DPBC) or as part of the newer Intelligent Mail Barcode (IMB).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/DeliveryPointCodeSet
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/isMemberOf
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#string
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/hasTag
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://pe.usps.com/cpim/ftp/pubs/Pub28/pub28.pdf
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/DeliveryPointCode
sources:
- id: fibo-source-e1b8af13cf
  resource: references/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
  sha256: e1b8af13cfbd56c65e428ff820890c7d7d5b5057af269667e5305e15ef80b1c6
  title: FIBO source FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
title: delivery point code
type: Ontology Class
---

# delivery point code

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/DeliveryPointCode>

## Definition

specific set of digits between 00 and 99 assigned to a delivery point

## Relationships

- **See also**: [pub28.pdf](<https://pe.usps.com/cpim/ftp/pubs/Pub28/pub28.pdf>)
- **Subclass of**: [CodeElement](<https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement>)

## Constraints

- **[isMemberOf](<https://www.omg.org/spec/Commons/Collections/isMemberOf>)**: exact qualified cardinality 1 of type [DeliveryPointCodeSet](/concepts/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses/DeliveryPointCodeSet.md)
- **[hasTag](<https://www.omg.org/spec/Commons/Designators/hasTag>)**: exact qualified cardinality 1 of type [string](<http://www.w3.org/2001/XMLSchema#string>)

## Annotations

- **label**: delivery point code
- **definition**: specific set of digits between 00 and 99 assigned to a delivery point
- **explanatoryNote**: When combined with the ZIP + 4 code, the delivery point code provides a unique identifier for every deliverable address served by the USPS. The delivery point digits are almost never printed on mail in human-readable form; instead they are encoded in the POSTNET delivery point barcode (DPBC) or as part of the newer Intelligent Mail Barcode (IMB).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
