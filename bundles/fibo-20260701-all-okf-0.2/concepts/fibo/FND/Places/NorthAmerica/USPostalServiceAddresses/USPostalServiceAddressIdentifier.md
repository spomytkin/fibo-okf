---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: U.S. Postal Service address identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: combined with the ZIP + 4 code, the delivery point code provides a unique identifier for every deliverable address
      served by the USPS
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The delivery point digits are almost never printed on mail in human-readable form; instead they are encoded in
      the POSTNET delivery point barcode (DPBC) or as part of the newer Intelligent Mail Barcode (IMB).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/DeliveryPointCode
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/ZIPPlus4Code
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/comprises
  subclass_of:
  - concept: /concepts/fibo/FND/Places/Addresses/PhysicalAddressIdentifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PhysicalAddressIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/USPostalServiceAddressIdentifier
sources:
- id: fibo-source-e1b8af13cf
  resource: references/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
  sha256: e1b8af13cfbd56c65e428ff820890c7d7d5b5057af269667e5305e15ef80b1c6
  title: FIBO source FND/Places/NorthAmerica/USPostalServiceAddresses.rdf
title: U.S. Postal Service address identifier
type: Ontology Class
---

# U.S. Postal Service address identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Places/NorthAmerica/USPostalServiceAddresses/USPostalServiceAddressIdentifier>

## Definition

combined with the ZIP + 4 code, the delivery point code provides a unique identifier for every deliverable address served by the USPS

## Relationships

- **Subclass of**: [PhysicalAddressIdentifier](/concepts/fibo/FND/Places/Addresses/PhysicalAddressIdentifier.md)

## Constraints

- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 1 of type [DeliveryPointCode](/concepts/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses/DeliveryPointCode.md)
- **[comprises](<https://www.omg.org/spec/Commons/Collections/comprises>)**: exact qualified cardinality 1 of type [ZIPPlus4Code](/concepts/fibo/FND/Places/NorthAmerica/USPostalServiceAddresses/ZIPPlus4Code.md)

## Annotations

- **label**: U.S. Postal Service address identifier
- **definition**: combined with the ZIP + 4 code, the delivery point code provides a unique identifier for every deliverable address served by the USPS
- **explanatoryNote**: The delivery point digits are almost never printed on mail in human-readable form; instead they are encoded in the POSTNET delivery point barcode (DPBC) or as part of the newer Intelligent Mail Barcode (IMB).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
